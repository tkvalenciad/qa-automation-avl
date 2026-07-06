import requests

from api_tests.helpers.evidence import record_api_exchange


class ApiClient:

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/")
        self._session = requests.Session()
        self._session.headers["Content-Type"] = "application/json"

    def request(self, method, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"

        response = self._session.request(
            method=method.upper(),
            url=url,
            json=payload,
        )

        record_api_exchange(method, url, payload, response)
        return response

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self._session.close()
        return False
