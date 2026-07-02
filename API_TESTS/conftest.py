import pytest
import random

from API_TESTS.http_client import HttpClient
from API_TESTS.openbrewery_api.openbrewery_service import BreweriesService
from API_TESTS.dog_api.dog_service import DogService
from API_TESTS.jsonplaceholder_api.jsonplaceholder_service import JsonplaceholderService


@pytest.fixture
def breweries_service():
    client = HttpClient("https://api.openbrewerydb.org/v1")
    return BreweriesService(client)


@pytest.fixture
def dog_service():
    client = HttpClient("https://dog.ceo/api")
    return DogService(client)


@pytest.fixture
def jsonplaceholder_service():
    client = HttpClient("https://jsonplaceholder.typicode.com")
    return JsonplaceholderService(client)


@pytest.fixture
def random_id():
    return random.randint(1, 100)


def pytest_addoption(parser):
    parser.addoption("--url", default="https://ya.ru")
    parser.addoption("--status_code", default=200, type=int)


@pytest.fixture(scope="session")
def url(pytestconfig):
    return pytestconfig.getoption("--url")


@pytest.fixture(scope="session")
def status_code(pytestconfig):
    return pytestconfig.getoption("--status_code")
