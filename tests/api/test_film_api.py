from api.api_manager import APIManager

class TestAPI:
    def test_all_films(self, api_manager: APIManager):
        """
        Positive test to get all films
        """
        response = api_manager.movies_api.get_list_movies()

    def test_all_films_with_params(self, api_manager: APIManager):
        """
        films with params
        """
        response = api_manager.movies_api.get_list_movies(params={"location": "SPB"})

    def test_add_new_film(self, api_manager: APIManager, new_film, auth_session, create_film):
        """
        Add new film
        """
        response = create_film # создал текстуру под создание фильма, чтобы вытащить id
        # схема: создаю фильм -> получаю id -> удаляю фильм по этому id = безотходное произодство

    def test_delete_film(self, api_manager: APIManager, create_film, auth_session):
        """
        Delete film
        """
        id_film = create_film["film_id"]
        response = api_manager.movies_api.delete_movie(id_film, auth_session)

    def test_deleted_film(self, api_manager: APIManager, create_film, auth_session):
        """
        Check if film is deleted
        """
        id_film = create_film["film_id"]
        response = api_manager.movies_api.get_movie_by_id(id_film)
