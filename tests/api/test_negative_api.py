from api.api_manager import APIManager
from conftest import create_film, new_film
from utils.datagenerator import DataGenetator


class TestNegativeApi:
    def test_get_film_by_params(self, api_manager: APIManager):
        api_manager.movies_api.get_list_movies(
            params={"locations": "ABC"},
            expected_status_code=400,
        )

    def test_create_film_without_auth(self,new_film, api_manager: APIManager):

        api_manager.movies_api.creating_new_movie(
            expected_status_code=401,
            **new_film
        )
    def test_delete_film_without_auth(self, api_manager: APIManager):

        api_manager.movies_api.delete_movie(
            movie_id=1,
            expected_status_code=401,
        )

    def test_movies_by_id(self, api_manager: APIManager):

        response = api_manager.movies_api.get_list_movies().json()
        all_films = response.get("movies")
        max_id = max(movie.get("id") for movie in all_films)

        api_manager.movies_api.get_movie_by_id(
            movie_id=max_id+10,
            expected_status_code=404,
        )