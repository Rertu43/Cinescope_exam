import logging
import requests


class CustomRequester():
    def __init__(self, base_url, session):
        self.base_url = base_url
        self.session = session
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

    def send_request(self,
                     method,
                     endpoint,
                     data=None,
                     expected_status=200,
                     params=None,
                     need_logging=True,
                     **kwargs):
        base_url = f"{self.base_url}{endpoint}"
        headers = kwargs.pop("headers", None)

        response = self.session.request(
            method=method,
            url=base_url,
            json=data,
            params=params,
            headers=headers,
        )

        if not isinstance(expected_status, (list, tuple)):
            expected_status = [expected_status]

        if response.status_code not in expected_status:
            raise ValueError(f"Unexpected status code {response.status_code}    "
                             f"Expected {expected_status}")
        if need_logging:
            self.log_request_and_response(response)
        return response

    def log_request_and_response(self, response):
        print("==============REQUEST==============")
        print(response.request.method)
        print(response.request.url)
        print(response.request.headers)
        if response.request.body:
            print(response.request.body)
        print("==============RESPONSE==============")
        print(response.status_code)
        print(response.text)

    def _update_session_headers(self, **headers):
        """
        :param session: Object request.Session, предоставленный API-классом
        """
        self.session.headers.update(headers)