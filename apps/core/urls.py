#Libs
from django.urls    import path,include
from rest_framework import routers


#Views
from apps.core  import views

router = routers.DefaultRouter()

router.register('produto',views.ProdutoViews)
router.register('produto-imagen',views.ProdutoImagensViews)
router.register('marca',views.MarcaViews)
router.register('categoria',views.CategoriaViews)
router.register('tags',views.TagsViews)
router.register('cliente',views.ClienteViews)
router.register('vendedor',views.VendedorViews)
router.register('pedido-venda',views.PedidoVendaViews)
router.register('carrinho',views.CarrinhoViews)


urlpatterns = [
 path('',include(router.urls),name='rest_core')   
]