#Libs
from rest_framework import viewsets


#Models
from apps.core import models

#Serializers
from apps.core import serializers



class ProdutoViews(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    
    def perform_create(self, serializer): 
        #Gravando o usuario da inclusao
        serializer.save(user=self.request.user)



class ProdutoImagensViews(viewsets.ModelViewSet):
    queryset = models.ProdutoImagens.objects.all()
    serializer_class = serializers.ItensPedidoVendaSerializer


class MarcaViews(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer


class CategoriaViews(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer


class TagsViews(viewsets.ModelViewSet):
    queryset = models.Tags.objects.all()
    serializer_class = serializers.TagsSerializer
   
            
class ClienteViews(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
  

class VendedorViews(viewsets.ModelViewSet):
    queryset = models.Vendedor.objects.all()
    serializer_class = serializers.VendedorSerializer
   
        
class PedidoVendaViews(viewsets.ModelViewSet):
    queryset = models.PedidoVenda.objects.all()
    serializer_class = serializers.PedidoVendaSerializer
   
        
class ItensPedidoVendaViews(viewsets.ModelViewSet):
    queryset = models.ItensPedidoVenda.objects.all()
    serializer_class = serializers.ItensPedidoVendaSerializer
   