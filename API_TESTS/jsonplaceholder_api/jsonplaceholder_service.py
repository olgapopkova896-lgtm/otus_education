from pydantic import TypeAdapter
from API_TESTS.jsonplaceholder_api.models.jsonplaceholder import Post, Comment, Update


class JsonplaceholderService:
    def __init__(self, http_client):
        self.http_client = http_client

    def get_posts(self):
        path = "posts"
        response = self.http_client.get(f"{path}")
        return TypeAdapter(list[Post]).validate_python(response)

    def get_one_post(self, post_id):
        path = f"posts/{post_id}"
        response = self.http_client.get(f"{path}")
        return Post.model_validate(response)

    def get_comments(self, post_id):
        path = f"posts/{post_id}/comments"
        response = self.http_client.get(f"{path}")
        return TypeAdapter(list[Comment]).validate_python(response)

    def post_resources(self, body):
        path = "posts"
        response = self.http_client.post(f"{path}", body=body)
        return Post.model_validate(response)

    def put_resources(self, body, post_id):
        path = f"posts/{post_id}"
        response = self.http_client.put(f"{path}", body=body)
        return Update.model_validate(response)

    def patch_resource(self, body, post_id):
        path = f"posts/{post_id}"
        response = self.http_client.patch(f"{path}", body=body)
        return Update.model_validate(response)

    def delete_resource(self, post_id):
        path = f"posts/{post_id}"
        response = self.http_client.delete(f"{path}")
        return response
