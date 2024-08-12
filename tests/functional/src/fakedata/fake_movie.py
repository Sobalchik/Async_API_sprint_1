import uuid

from faker import Faker

from .base_models import FakeMovie
from ...settings import test_settings

class FakeMovieData:
    def __init__(self, person_generator, genre_generator):
        self.fake = Faker()
        self.person_generator = person_generator
        self.genre_generator = genre_generator

    def _generate_persons(self, movie_id):
        actors = self.person_generator.generate_people(2, movie_id)
        writers = self.person_generator.generate_people(2, movie_id)
        directors = self.person_generator.generate_people(1, movie_id)
        return actors, writers, directors

    def _generate_genres(self, movie_id):
        return self.genre_generator.generate_genres(2, movie_id)

    def _generate_movie_data(self, movie_id):
        if movie_id is None:
            movie_id = str(uuid.uuid4())
        actors, writers, directors = self._generate_persons(movie_id)
        genres = self._generate_genres(movie_id)
        return {
            "_id": movie_id,
            "_index": test_settings.es_index_movies,
            "_source": FakeMovie(
                id=movie_id,
                title=self.fake.sentence(nb_words=3, variable_nb_words=False),
                imdb_rating=round(self.fake.random.uniform(1, 10), 1),
                description=self.fake.text(max_nb_chars=10),
                genres=[genre["_source"]["name"] for genre in genres],
                actors=[{"id": actor["_id"], "name": actor["_source"]["full_name"]} for actor in actors],
                actors_names=[actor["_source"]["full_name"] for actor in actors],
                writers=[
                    {"id": writer["_id"], "name": writer["_source"]["full_name"]} for writer in writers
                ],
                writers_names=[writer["_source"]["full_name"] for writer in writers],
                directors=[
                    {"id": director["_id"], "name": director["_source"]["full_name"]}
                    for director in directors
                ],
            ).model_dump(),
        }

    def generate_movie(self, movie_id=None):
        return self._generate_movie_data(movie_id)

    def generate_movies(self, count=10, movie_id=None):
        return [self.generate_movie(movie_id=None) for _ in range(count)]
