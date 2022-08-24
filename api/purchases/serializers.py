from rest_framework import serializers


class UserPurchaseSerializer(serializers.Serializer):
    product = serializers.CharField(source='product.title', max_length=200)
    count = serializers.IntegerField()
