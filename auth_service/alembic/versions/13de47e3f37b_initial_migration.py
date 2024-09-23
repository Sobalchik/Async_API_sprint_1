"""Initial migration

Revision ID: 13de47e3f37b
Revises: 
Create Date: 2024-09-23 21:21:31.056497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13de47e3f37b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='auth'
    )
    op.create_table('user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.Text(), nullable=False),
    sa.Column('password', sa.Text(), nullable=False),
    sa.Column('email', sa.Text(), nullable=False),
    sa.Column('role_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['auth.role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username'),
    schema='auth'
    )
    op.create_table('login_history',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('logged_in_at', sa.DateTime(), nullable=False),
    sa.Column('user_agent', sa.Text(), nullable=True),
    sa.Column('user_device_type', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['auth.user.id'], ),
    sa.PrimaryKeyConstraint('id', 'user_device_type'),
    sa.UniqueConstraint('id', 'user_device_type'),
    schema='auth',
    postgresql_partition_by='LIST (user_device_type)'
    )
    op.create_table('social_user',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('social_user_id', sa.UUID(), nullable=False),
    sa.Column('social_type', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['auth.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'social_user_id'),
    schema='auth'
    )
    # Create partitions
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS auth.login_history_in_smart
        PARTITION OF auth.login_history FOR VALUES IN ('smart');
        """
    )

    op.execute(
        """
        CREATE TABLE IF NOT EXISTS auth.login_history_in_mobile
        PARTITION OF auth.login_history FOR VALUES IN ('mobile');
        """
    )

    op.execute(
        """
        CREATE TABLE IF NOT EXISTS auth.login_history_in_web
        PARTITION OF auth.login_history FOR VALUES IN ('web');
        """
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("DROP TABLE IF EXISTS auth.login_history_in_smart;")
    op.execute("DROP TABLE IF EXISTS auth.login_history_in_mobile;")
    op.execute("DROP TABLE IF EXISTS auth.login_history_in_web;")

    op.drop_table('social_user', schema='auth')
    op.drop_table('login_history', schema='auth')
    op.drop_table('user', schema='auth')
    op.drop_table('role', schema='auth')
    # ### end Alembic commands ###
