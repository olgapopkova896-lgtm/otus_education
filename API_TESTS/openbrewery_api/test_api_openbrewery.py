import pytest
import random

from API_TESTS.openbrewery_api.data.brewery_data import brewery_1


@pytest.mark.api
def test_list_breweries(breweries_service):
    response = breweries_service.get_list_breweries()
    assert response[1].model_dump() == brewery_1, f'Response must be {brewery_1}'


@pytest.mark.api
def test_single_brewery(breweries_service):
    response = breweries_service.get_single_brewery(brewery_1["id"])
    assert response.model_dump() == brewery_1, f'Response must be {brewery_1}'


by_type = random.choice([
    "micro", "nano", "regional", "brewpub", "large", "planning", "bar", "contract", "proprietor", "closed"])
random_page = random.randint(1, 100)
random_per_page = random.randint(1, 200)
sort_by = random.choice(["asc", "desc"])


@pytest.mark.api
@pytest.mark.parametrize(
    ("filter_name", "filter_value", "expected_field", "expected_value"),
    [
        pytest.param("by_city", "san_diego", "city", "San Diego", id="by_city: San Diego"),
        pytest.param("by_country", "belgium", "country", "Belgium", id="by_country: Belgium"),
        pytest.param("by_state", "california", "state", "California", id="by_state: California"),
        pytest.param("by_type", by_type, "brewery_type", by_type, id=f"by_type: {by_type}"),

    ]
)
def test_query_parameters(filter_name, filter_value, expected_field, expected_value, breweries_service):
    response = breweries_service.get_by_filter(filter_name, filter_value)
    assert len(response) > 0, f'Response length should be more then zero, actual is {len(response)}'
    assert any(getattr(item, expected_field) == expected_value for item in
               response), f'Response must contain {expected_field}: {expected_value}'


def test_random_brewery(breweries_service):
    random_number = random.randint(1, 50)
    response = breweries_service.get_random_brewery(random_number)
    assert isinstance(response, list), f'Response must be in list type, actual is {type(response)}'
    assert len(response) == random_number, f'Number of brewery in must be {random_number}, actual is {len(response)}'


@pytest.mark.api
@pytest.mark.parametrize(
    "search_value",
    [
        pytest.param("Hockley Valley Brewing Co", id="Hockley Valley Brewing Co"),
        pytest.param("Brew", id="Brew"),
        pytest.param("Dog", id="Dog"),
    ],
)
def test_search(search_value, breweries_service):
    response = breweries_service.get_search(search_value)
    assert any(search_value.lower() in item.name.lower() for item in response), f'Response must have {search_value} in name, city or country'


def test_search_no_result(breweries_service):
    response = breweries_service.get_search("1111111")
    assert response == [], 'Response must be empty after delete'
