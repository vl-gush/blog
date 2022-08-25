import pytest

from django.test.client import Client

from shop.models import Purchase, Product
from tests.factories import UserFactory, PurchaseFactory, ProductFactory


@pytest.mark.django_db
class TestPurchasesViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()

    def test_product_list(self):
        ProductFactory(cost=30)
        response = self.client.get("/api/products/?min_cost=50")
        assert response.status_code == 200
        assert response.data["count"] == 0

        ProductFactory(cost=70)
        response = self.client.get("/api/products/?min_cost=50")
        assert response.status_code == 200
        assert response.data["count"] == 1

    def test_product_search_and_filter(self):
        cost = 50
        for i in range(3):
            ProductFactory(color='red', cost=cost)
            cost += 50

        cost = 50
        for i in range(4):
            ProductFactory(color='green', cost=cost)
            cost += 50
        cost = 50
        for i in range(5):
            ProductFactory(color='white', cost=cost)
            cost += 50

        response = self.client.get("/api/products/?search=white")
        assert response.status_code == 200
        assert response.data["count"] == 5

        response = self.client.get("/api/products/?min_cost=150")
        assert response.status_code == 200
        assert response.data["count"] == 6

        response = self.client.get("/api/products/?search=green&min_cost=100")
        assert response.status_code == 200
        assert response.data["count"] == 3

        assert Product.objects.count() == 12

    def test_purchases_list(self):
        purchase_1 = PurchaseFactory()
        self.client.force_login(purchase_1.user)
        response = self.client.get("/api/purchases/")

        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["product"]["title"] == purchase_1.product.title

        purchase_2 = PurchaseFactory(user=self.user)
        self.client.force_login(self.user)
        response = self.client.get("/api/purchases/")

        assert response.status_code == 200
        assert response.data["count"] == 1
        assert response.data["results"][0]["product"]["title"] == purchase_2.product.title

        assert Purchase.objects.count() == 2
