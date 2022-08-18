import pytest

from django.test.client import Client

from tests.factories import PostFactory, MyModelFactory



@pytest.mark.django_db
class TestViews:

    def setup_method(self):
        self.client = Client()

    def test_post_list(self):
        PostFactory.create_batch(5)
        response = self.client.get("/api/posts/")

        assert response.status_code == 200
        assert len(response.data) == 5

    def test_post_create(self):
        data = {"title": "title", "slug": "slug", "text": "text"}
        response = self.client.post("/api/posts/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data) == 1


@pytest.mark.django_db
class TestMyModelViews:

    def setup_method(self):
        self.client = Client()

    def test_my_module_list(self):
        MyModelFactory.create_batch(5)
        response = self.client.get("/api/myapp/")

        assert response.status_code == 200
        assert len(response.data) == 5

    def test_my_model_create(self):
        data = {"title": "title", "slug": "slug", "text": "text"}
        response = self.client.post("/api/myapp/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/myapp/")
        assert response.status_code == 200
        assert len(response.data) == 1
