import pytest
from API_TESTS.jsonplaceholder_api.data.jsonplaceholder_data import post_1

@pytest.mark.api
def test_all_posts(jsonplaceholder_service):
    response = jsonplaceholder_service.get_posts()
    assert response[1].model_dump() == post_1, f'Response must be {post_1}'


@pytest.mark.api
def test_one_post(random_id,jsonplaceholder_service):
    response = jsonplaceholder_service.get_one_post(random_id)
    assert response.id == random_id, f'Response id must be {random_id}, actual is {response.id}'

@pytest.mark.api
def test_comments(random_id, jsonplaceholder_service):
    response = jsonplaceholder_service.get_comments(random_id)
    assert all(item.postId == random_id for item in response), f'Response postId must be {random_id}'


@pytest.mark.api
@pytest.mark.parametrize(
    "body",
    [
        pytest.param({"title": "one", "body": "no", "userId": 1}, id="1"),
        pytest.param({"title": "two", "body": "test", "userId": 2}, id="2"),
    ],
)
def test_creating_resource(body, jsonplaceholder_service):
    response = jsonplaceholder_service.post_resources(body)
    assert response.title == body['title'], f'title in response must be {body['title']}'
    assert response.body == body['body'], f'body in response must be {body['body']}'
    assert response.userId == body['userId'], f'userId in response must be {body['userId']}'


@pytest.mark.api
def test_updating_resource(random_id, jsonplaceholder_service):
    body_update = {"id": random_id, "title": "foo", "body": "bar", "userId": 1}
    response = jsonplaceholder_service.put_resources(body_update, random_id)
    assert response.id == body_update['id'], f'id in response must be {body_update['id']}'
    assert response.title == body_update['title'], f'title in response must be {body_update['title']}'
    assert response.body == body_update['body'], f'body in response must be {body_update['body']}'
    assert response.userId == body_update['userId'], f'userId in response must be {body_update['userId']}'


@pytest.mark.api
@pytest.mark.parametrize(
    ('id_up', 'field', 'value'),
    [
        pytest.param(1, "title", "one", id="1_title"),
        pytest.param(5, "body", "two", id="2_body"),
        pytest.param(17, "userId", 5555, id="17_userId"),
    ],
)
def test_patching_resource(id_up, field, value, random_id, jsonplaceholder_service):
    body_update = {"id": id_up, field: value}
    response = jsonplaceholder_service.patch_resource(body_update, id_up)
    assert getattr(response, field) == value, f'{field} in response must be {value}'
    assert response.id == id_up, f'id in response must be {id_up}'


def test_delete_resource(random_id, jsonplaceholder_service):
    response = jsonplaceholder_service.delete_resource(random_id)
    assert response == {}, 'resource must be deleted'
