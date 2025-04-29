import pytest
import requests
from datetime import datetime
from faker import Faker
from constants import BASE_URL, REGISTER_URL

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
    created_at = datetime.utcnow().isoformat(timespec="milliseconds") + "Z"
    fake = Faker()
    return {
        "name": fake.sentence(nb_words=3),
        "price": fake.random_int(min=100, max=1000),
        "description": fake.text(),
        "imageUrl": "https://placekitten.com/300/300",
        "location": "MSK",
        "published": True,
        "genreId": fake.random_int(min=1, max=10)  # предполагаем, что жанры от 1 до 10
    }


@pytest.fixture(scope="session")
def new_user():
    """
    Fixture for creating a new user
    """
    faker = Faker()
    email = faker.email()
    name = faker.name()
    password = faker.password()

    return {
        "email": email,
        "fullName": name,
        "password": password,
        "passwordRepeat": password,
    }


@pytest.fixture(scope="session")
def auth_session(new_user):

    log_url = f"{REGISTER_URL}/login"
    log_payload = {
        "email": "test-admin@mail.com",
        "password": "KcLMmxkJMjBD1",
    }
    response = requests.post(log_url, json=log_payload)
    token = response.json().get("accessToken")
    assert token is not None, "Error with token"
    assert response.status_code == 200, "Error with login"


    return token

@pytest.fixture(scope="session")
def create_film(api_manager: APIManager, new_film, auth_session):
    response = api_manager.movies_api.creating_new_movie(auth_session, **new_film)

    return {
        "response": response,
        "film_id": response.json().get("id"),
    }

