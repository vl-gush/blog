import factory
from factory.django import DjangoModelFactory

from posts.models import Post
from myapp.models import MyModel


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("word")
    slug = factory.Faker("word")
    text = factory.Faker("sentence")


class MyModelFactory(DjangoModelFactory):
    class Meta:
        model = MyModel

    title = factory.Faker("word")
    slug = factory.Faker("word")
    text = factory.Faker("sentence")
