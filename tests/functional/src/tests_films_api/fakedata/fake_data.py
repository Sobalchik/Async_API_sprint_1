from .base_models import FakeGenre, FakeMovie, FakePerson
from .fake_genre import FakeGenreData
from .fake_movie import FakeMovieData
from .fake_person import FakePersonData


class FakeData:

    def __init__(self) -> None:
        self.fake_genre_data = FakeGenreData()
        self.fake_person_data = FakePersonData()
        self.__fake_movie_data = FakeMovieData()

    def generate_data(self, count: int = 10) -> tuple[list, list, list]:
        data = self.__fake_movie_data.generate_movies(count=count, bundle=True)
        movies = []
        genres = []
        persons = []
        for item in data:
            movies.append(item["movies"])
            genres.extend([*item["genres"]])
            persons.extend([*item["persons"]])
        return movies, genres, persons

    def transform_to_es(
        self,
        movies: list[FakeMovie],
        genres: list[FakeGenre],
        persons: list[FakePerson],
    ) -> tuple[list, list, list]:
        return (
            self.__fake_movie_data.transform_to_es(movies),
            self.fake_genre_data.transform_to_es(genres),
            self.fake_person_data.transform_to_es(persons),
        )
