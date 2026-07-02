import pytest
import random


@pytest.mark.api
def test_dog_api_list_all_breeds(dog_service):
    response = dog_service.get_all_breeds()
    assert response.message['retriever'] == ['chesapeake', 'curly', 'flatcoated',
                                             'golden'], "Message in response must have sub-breeds 'chesapeake', 'curly', 'flatcoated', 'golden' for breed 'retriever'"
    assert response.message['beagle'] == [], "Message in response must not have any sub-breeds for breed 'beagle'"


@pytest.mark.api
def test_dog_api_single_all_breeds_image_random(dog_service):
    response = dog_service.get_breeds_image_random()
    assert response.message.startswith(
        f"https://images.dog.ceo/breeds/"), "Image link in message must start with 'https://images.dog.ceo/breeds/'"
    assert response.message.endswith(".jpg"), "Image file in message must be '.jpg'"


@pytest.mark.api
def test_dog_api_multiple_all_breeds_images_random(dog_service):
    image_number = random.randint(1, 50)
    response = dog_service.get_multiple_breeds_images_random(image_number)
    assert len(
        response.message) == image_number, f"Number of image must be {image_number}, actual is {len(response.message)}"


@pytest.mark.api
@pytest.mark.parametrize(
    ("breed", "expected_image"),
    [
        pytest.param("retriever", "https://images.dog.ceo/breeds/retriever-chesapeake/n02099849_1024.jpg",
                     id="retriever"),
        pytest.param("beagle", "https://images.dog.ceo/breeds/beagle/n02088364_10108.jpg", id="beagle")
    ]
)
def test_dog_api_all_images_for_breeds(breed, expected_image, dog_service):
    response = dog_service.get_images_for_breeds(breed)
    assert expected_image in response.message, f"Message in response must have image {expected_image}"


@pytest.mark.api
@pytest.mark.parametrize(
    "breed",
    [
        pytest.param("retriever", id="retriever"),
        pytest.param("beagle", id="beagle")
    ]
)
def test_dog_api_single_random_breed_image(breed, dog_service):
    response = dog_service.get_single_random_breed_image(breed)
    assert response.message.startswith(
        f"https://images.dog.ceo/breeds/{breed}"), f"Image link in message must start with 'https://images.dog.ceo/breeds/{breed}'"
    assert response.message.endswith(".jpg"), "Image file in message must be '.jpg'"


@pytest.mark.api
@pytest.mark.parametrize(
    "breed",
    [
        pytest.param("retriever", id="retriever"),
        pytest.param("beagle", id="beagle")
    ]
)
def test_dog_api_multiple_random_breeds_images(breed, dog_service):
    image_number = random.randint(1, 20)
    response = dog_service.get_multiple_random_breed_images(breed, image_number)
    assert len(response.message) == image_number


@pytest.mark.api
@pytest.mark.parametrize(
    ("breed", "sub_breeds"),
    [
        pytest.param("retriever", ["chesapeake", "curly", "flatcoated", "golden"], id="retriever"),
        pytest.param("beagle", [], id="beagle")
    ]
)
def test_dog_api_list_all_sub_breeds(breed, sub_breeds, dog_service):
    response = dog_service.get_list_all_sub_breeds(breed)
    assert response.message == sub_breeds


@pytest.mark.api
@pytest.mark.parametrize(
    ("breed", "sub_breed", "image"),
    [
        pytest.param("african", "wild", "https://images.dog.ceo/breeds/african-wild/n02116738_10081.jpg",
                     id="african-wild"),
        pytest.param("retriever", "golden", "https://images.dog.ceo/breeds/retriever-golden/Mori_1.jpg",
                     id="retriever-golden")
    ]
)
def test_dog_api_list_sub_breeds_images(breed, sub_breed, image, dog_service):
    response = dog_service.get_list_sub_breeds_images(breed, sub_breed)
    assert image in response.message


@pytest.mark.api
@pytest.mark.parametrize(
    ("breed", "sub_breed"),
    [
        pytest.param("african", "wild", id="african-wild"),
        pytest.param("retriever", "golden", id="retriever-golden"),
    ]
)
def test_dog_api_single_random_sub_breeds_image(breed, sub_breed, dog_service):
    response = dog_service.get_single_random_sub_breeds_image(breed, sub_breed)
    assert response.message.startswith(
        f"https://images.dog.ceo/breeds/{breed}-{sub_breed}"), f"Image link in message must start with 'https://images.dog.ceo/breeds/{breed}-{sub_breed}'"
    assert response.message.endswith(".jpg"), "Image file in message must be '.jpg'"


@pytest.mark.api
@pytest.mark.parametrize(
    ("breed", "sub_breed"),
    [
        pytest.param("african", "wild", id="african-wild"),
        pytest.param("retriever", "golden", id="retriever-golden")
    ]
)
def test_dog_api_multiple_random_sub_breeds_images(breed, sub_breed, dog_service):
    image_number = random.randint(1, 20)
    response = dog_service.get_multiple_random_sub_breeds_images(breed, sub_breed, image_number)
    assert len(response.message) == image_number
