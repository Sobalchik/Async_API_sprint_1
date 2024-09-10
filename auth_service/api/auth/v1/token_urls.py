from datetime import timedelta

from async_fastapi_jwt_auth import AuthJWT
from fastapi import APIRouter, Depends, HTTPException, Request, Response
from redis.asyncio import Redis

from core.config.components.settings import Settings, User
from core.config.components.token_conf import Tokens, get_tokens
from db.redis import get_redis
from hash import hash_data
from services.user_service import UserService, get_user

router = APIRouter()


@AuthJWT.load_config
def get_config():
    return Settings()


@router.get("/refresh")
async def refresh(
    request: Request,
    response: Response,
    tokens: Tokens = Depends(get_tokens),
    user: UserService = Depends(get_user),
    redis_client: Redis = Depends(get_redis),
):
    user = user.get_user(await tokens.validate_refresh())
    user_agent = request.headers.get("user-agent")
    byte_agent = bytes(user_agent, encoding="utf-8")
    access_token, refresh_token = await tokens.refresh(user=user, response=response)

    await redis_client.set(
        name=f"access_token:{user.login}:{hash_data(byte_agent)}",
        ex=timedelta(minutes=10),
        value=access_token,
    )
    await redis_client.set(
        name=f"refresh_token:{user.login}:{hash_data(byte_agent)}",
        ex=timedelta(days=10),
        value=refresh_token,
    )
    return {"msg": "Successfully logged in"}


@router.get("/user")
async def user(tokens: Tokens = Depends(get_tokens)):
    current_user = await tokens.validate()
    return {"user": current_user} if current_user is not None else 404


@router.get("/validate_token")
async def check_redis(
    request: Request,
    redis: Redis = Depends(get_redis),
    tokens: Tokens = Depends(get_tokens),
    user: UserService = Depends(get_user),
):
    refresh_token = request.cookies.get("refresh_token_cookie")
    user = user.get_user(await tokens.validate())
    user_agent = request.headers.get("user-agent")
    byte_agent = bytes(user_agent, encoding="utf-8")
    rf_in_redis = await redis.get(f"refresh_token:{user.login}:{hash_data(byte_agent)}")
    if rf_in_redis.decode() == str(refresh_token):
        return {"msg": "Successfully validation"}
    raise HTTPException(status_code=401, detail="Unauthorized")