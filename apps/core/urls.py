#Libs
from django.urls    import path,include
from rest_framework import routers


#Views
from apps.core  import views

router = routers.DefaultRouter()

router.register('produto',views.ProdutoViews)

urlpatterns = [
 path('',include(router.urls),name='rest_core')   
]