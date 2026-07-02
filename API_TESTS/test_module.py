import requests


def test_status_code(url, status_code):
    response = requests.get(url)
    print(response)
    assert response.status_code == status_code, f'Status code must be {status_code}, actual is {response.status_code}'