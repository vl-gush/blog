from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from api.purchases.serializers import UserPurchaseSerializer
from shop.models import Purchase


class GetPurchaseViewSet(ListAPIView):
    serializer_class = UserPurchaseSerializer

    def get_queryset(self):
        username = self.request.user
        return Purchase.objects.filter(user=username)
