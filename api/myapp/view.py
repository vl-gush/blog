from rest_framework import viewsets, status
from rest_framework.response import Response

from api.myapp.serializers import MyModelSerializer
from myapp.models import MyModel


class MyModelViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed.
    """

    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        MyModel.objects.create(**serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)
