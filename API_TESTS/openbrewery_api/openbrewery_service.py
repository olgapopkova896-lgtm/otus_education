from pydantic import TypeAdapter
from API_TESTS.openbrewery_api.models.breweries import Brewery


class BreweriesService:
    def __init__(self, http_client):
        self.http_client = http_client

    def get_list_breweries(self):
        path = "breweries"
        response = self.http_client.get(f"{path}")
        return TypeAdapter(list[Brewery]).validate_python(response)

    def get_single_brewery(self, obdb_id):
        path = f'breweries/{obdb_id}'
        response = self.http_client.get(path)
        return Brewery.model_validate(response)

    def get_by_filter(self, filter_name, filter_value):
        path = "breweries"
        params = {filter_name: filter_value}
        response = self.http_client.get(path, params=params)
        return TypeAdapter(list[Brewery]).validate_python(response)

    def get_random_brewery(self, random_number):
        path = 'breweries/random'
        response = self.http_client.get(path, params={'size': random_number})
        return TypeAdapter(list[Brewery]).validate_python(response)

    def get_search(self, search_value):
        path = "breweries/search"
        params = {"query": search_value}
        response = self.http_client.get(path, params=params)
        return TypeAdapter(list[Brewery]).validate_python(response)
