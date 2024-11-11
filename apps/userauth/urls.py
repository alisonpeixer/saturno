#Libs
from django.urls import path,include
from rest_framework import routers

#Views
from apps.userauth import views


router = routers.DefaultRouter()

router.register('user',views.UserViewSet)


urlpatterns = [
    path('',include(router.urls),name='rest_user'),
    path('register',view=views.UserCreateView.as_view(), name='user_register')
]

