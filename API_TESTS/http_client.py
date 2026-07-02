from typing import Any
import requests


class HttpClient:
    def __init__(self, url: str) -> None:
        self.url = url

    def request(self, method, path: str, headers: dict = None, body: dict = None, code: int = 200,
                params: dict = None) -> dict[str, Any]:
        response = requests.request(method, f'{self.url}/{path}', params=params, headers=headers, json=body)
        assert response.status_code == code, f"Response status code must be {code}, actual is {response.status_code}"
        response_json = response.json()
        return response_json

    def get(self, path: str, code: int = 200, params: dict = None) -> dict[str, Any]:
        return self.request('GET', path=path, code=code, params=params)

    def post(self, path: str, headers: dict = None, body: dict = None, code: int = 201) -> dict[str, Any]:
        return self.request('POST', path=path, headers=headers, body=body, code=code)

    def put(self, path: str, headers: dict = None, body: dict = None, code: int = 200) -> dict[str, Any]:
        return self.request('PUT', path=path, headers=headers, body=body, code=code)

    def patch(self, path: str, headers: dict = None, body: dict = None, code: int = 200) -> dict[str, Any]:
        return self.request('PATCH', path=path, headers=headers, body=body, code=code)

    def delete(self, path: str, code: int = 200) -> dict[str, Any]:
        return self.request('DELETE', path=path, code=code)
