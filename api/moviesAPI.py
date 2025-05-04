from custom_requester.custom_requester import CustomRequester
from constants import BASE_URL


class MoviesAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def get_list_movies(self, params=None, expected_status_code=200):
        """
        Function to get a list of movies
        """
        return self.send_request(
            method='GET',
            endpoint='movies',
            params=params,
            expected_status=expected_status_code,
        )

    def get_movie_by_id(self, movie_id, expected_status_code=200):
        """
        Function to get a movie by ID
        """
        return self.send_request(
            method='GET',
            endpoint=f'movies/{movie_id}',
            expected_status=expected_status_code,
        )

    def creating_new_movie(self, expected_status_code=201, **kwargs):
        """
        Function to create a new movie
        """

        return self.send_request(
            method='POST',
            endpoint=f'movies',
            expected_status=expected_status_code,
            data=kwargs,
        )

    def delete_movie(self, movie_id, expected_status_code=200):
        """
        Function to delete a movie
        """
        return self.send_request(
            method="DELETE",
            endpoint=f'movies/{movie_id}',
            expected_status=expected_status_code,
        )