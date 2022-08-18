from rest_framework import serializers


class MyModelSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    slug = serializers.SlugField()
    text = serializers.CharField()
