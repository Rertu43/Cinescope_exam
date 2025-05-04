import pytest
import requests
from utils.datagenerator import DataGenetator

from api.api_manager import APIManager


@pytest.fixture(scope="session")
def session():
    """
    Fixture for creating a session
    """
    http_session = requests.Session()
    yield http_session
    http_session.close()


@pytest.fixture(scope="session")
def api_manager(session):
    """
    Fixture for creating api_manager
    """
    return APIManager(session)


@pytest.fixture(scope="session")
def new_film():
    return DataGenetator.data_for_film()

@pytest.fixture(scope="session")
def new_user():
    """
    Fixture for creating a new user
    """
    return DataGenetator.data_for_user()

@pytest.fixture
def user_session():
    user_pool = []

    def _create_user_session():
        session = requests.Session()
        user_session = APIManager(session)
        user_pool.append(user_session)
        return user_session

    yield _create_user_session

    for user in user_pool:
        user.close_session()

@pytest.fixture(scope="function")
def create_film(new_film, api_manager: APIManager):
    api_manager.auth_api.authenticate()
    response = api_manager.movies_api.creating_new_movie(**new_film).json()

    yield response

    id_film = response.get("id")
    assert id_film is not None, "Problems with getting id"
    response = api_manager.movies_api.delete_movie(id_film)


@pytest.fixture(scope="function")
def movie_lifecycle(new_film, api_manager: APIManager):

    api_manager.auth_api.authenticate()

    create_response = api_manager.movies_api.creating_new_movie(**new_film).json()
    film_id = create_response.get("id")

    try:
        api_manager.movies_api.get_movie_by_id(film_id)

    finally:
        api_manager.movies_api.delete_movie(film_id)

        api_manager.movies_api.get_movie_by_id(film_id, expected_status_code=404)