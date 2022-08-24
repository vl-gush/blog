from django.urls import include, path
from rest_framework import routers

from api.auth.views import RegisterView, LoginView, LogoutView
from api.posts.views import PostViewSet
from api.purchases.views import GetPurchaseViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("purchases/", GetPurchaseViewSet.as_view(), name="purchases"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
