from custom_requester.custom_requester import CustomRequester
from constants import BASE_URL
from constants import authorization_token


class MoviesAPI(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url=BASE_URL)

    def get_list_movies(self, **kwargs):
        """
        Function to get a list of movies
        """
        return self.send_request(
            method='GET',
            endpoint='/movies',
            params=kwargs,
        )

    def get_movie_by_id(self, movie_id):
        """
        Function to get a movie by ID
        """
        return self.send_request(
            method='GET',
            endpoint=f'/movies/{movie_id}',
            expected_status=404, # установлено для последнего теста, что фильм удален
        )

    def creating_new_movie(self, auth_sesion, **kwargs):
        """
        Function to create a new movie
        """
        return self.send_request(
            method='POST',
            endpoint=f'/movies',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {auth_sesion}',
            },
            expected_status=201,
            data=kwargs,
        )

    def delete_movie(self, movie_id, auth_sesion):
        """
        Function to delete a movie
        """
        return self.send_request(
            method="DELETE",
            endpoint=f'/movies/{movie_id}',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {auth_sesion}',}
        )