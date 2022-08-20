import factory
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from posts.models import Post


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("word")
    slug = factory.Faker("word")
    text = factory.Faker("sentence")


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("word")
    email = factory.Faker("email")
