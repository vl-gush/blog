import factory
from factory.django import DjangoModelFactory

from posts.models import Post


class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post

    title = factory.Faker("word")
    slug = factory.Faker("word")
    text = factory.Faker("sentence")
