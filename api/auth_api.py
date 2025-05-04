from requests import session

from custom_requester.custom_requester import CustomRequester
from constants import LOGIN_ENDPOINT


class AuthApi(CustomRequester):
    def __init__(self, session):
        super().__init__(session=session, base_url="https://auth.dev-cinescope.coconutqa.ru")

    def login_user(self, login_data, expected_status=200):
        """
        User authorization
        :param expected_status:
        :param login_data: data for login
        """
        return self.send_request(
            method="POST",
            endpoint=LOGIN_ENDPOINT,
            data=login_data,
            expected_status=expected_status,
        )


    def authenticate(self):
        login_data = {
            "email": "test-admin@mail.com",
            "password": "KcLMmxkJMjBD1"
        }

        response = self.login_user(login_data).json()
        if "accessToken" not in response:
            raise KeyError("token is missing")

        token = response["accessToken"]
        self._update_session_headers(authorization=f"Bearer {token}")