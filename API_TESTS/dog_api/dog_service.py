from API_TESTS.dog_api.models.breeds import DogBreedsResponse, DogSingleImageResponse, DogMultipleImageResponse


class DogService:
    def __init__(self,http_client) -> None:
        self.http_client = http_client


    def get_all_breeds(self):
        path = 'breeds/list/all'
        response = self.http_client.get(path)
        return DogBreedsResponse(**response)

    def get_breeds_image_random(self):
        path = 'breeds/image/random'
        response = self.http_client.get(path)
        return DogSingleImageResponse(**response)

    def get_multiple_breeds_images_random(self, image_number):
        path = f'breeds/image/random/{image_number}'
        response = self.http_client.get(path)
        return DogMultipleImageResponse(**response)

    def get_images_for_breeds(self, breed):
        path = f'breed/{breed}/images'
        response = self.http_client.get(path)
        return DogMultipleImageResponse(**response)

    def get_single_random_breed_image(self, breed):
        path = f'breed/{breed}/images/random'
        response = self.http_client.get(path)
        return DogSingleImageResponse(**response)

    def get_multiple_random_breed_images(self, breed, image_number):
        path = f'breed/{breed}/images/random/{image_number}'
        response = self.http_client.get(path)
        return DogMultipleImageResponse(**response)

    def get_list_all_sub_breeds(self, breed):
        path = f'breed/{breed}/list'
        response = self.http_client.get(path)
        return DogMultipleImageResponse(**response)

    def get_list_sub_breeds_images(self, breed, sub_breed):
        path = f'breed/{breed}/{sub_breed}/images'
        response = self.http_client.get(path)
        return DogMultipleImageResponse(**response)

    def get_single_random_sub_breeds_image(self, breed, sub_breed):
        path = f'breed/{breed}/{sub_breed}/images/random'
        response = self.http_client.get(path)
        return DogSingleImageResponse(**response)

    def get_multiple_random_sub_breeds_images(self, breed, sub_breed, image_number):
        path = f'breed/{breed}/{sub_breed}/images/random/{image_number}'
        response = self.http_client.get(path)
        return DogMultipleImageResponse(**response)


