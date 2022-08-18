from django.urls import include, path
from rest_framework import routers
from api.posts.views import PostViewSet
from api.myapp.view import MyModelViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'myapp', MyModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
