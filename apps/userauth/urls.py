#Libs
from django.urls import path,include
from rest_framework import routers

from dj_rest_auth.views import UserDetailsView
from .serializers import CustomUserDetailsSerializer,UserSerializer

#Views
from apps.userauth import views




router = routers.DefaultRouter()

router.register('user',views.UserViewSet)


urlpatterns = [
    path('',include(router.urls),name='rest_user'),
    path('register',view=views.UserCreateView.as_view(), name='user_register'),
    path('v1/', include("dj_rest_auth.urls")),
    path('custom/user/', UserDetailsView.as_view(serializer_class=UserSerializer)),
]

