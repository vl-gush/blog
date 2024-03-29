import factory
import factory.fuzzy
from django.contrib.auth.models import User
from factory.django import DjangoModelFactory

from posts.models import Post
from shop.models import Purchase, Product, COLOR_CHOICES


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


class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    title = factory.Faker("company")
    color = factory.fuzzy.FuzzyChoice(dict(COLOR_CHOICES).keys())
    cost = factory.Faker("pyint", min_value=50, max_value=150)


class PurchaseFactory(DjangoModelFactory):
    class Meta:
        model = Purchase

    user = factory.SubFactory(UserFactory)
    product = factory.SubFactory(ProductFactory)
    count = factory.Faker("pyint", min_value=1, max_value=5)
