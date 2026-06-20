import pytest


@pytest.fixture(scope="session")
def start_session():
    print("\n Start test execution")
    yield
    print("\n Stop test execution")


@pytest.fixture(scope="module")
def start_file(start_session):
    print("\n Start new .py file")
    yield
    print("\n End .py file")


@pytest.fixture(scope="function")
def start_test():
    print("\n Start test")
    yield
    print("\n End test")
