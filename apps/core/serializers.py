#Libs
from rest_framework import serializers


#Models
from apps.core import models

class ProdutoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Produto
        fields = '__all__'

class ProdutoImagensSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.ProdutoImagens
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.Marca
        fields = '__all__'
        
class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.Categoria
        fields = '__all__'
    
class TagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.Tags
        fields = '__all__'
            
class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.Cliente
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.Vendedor
        fields = '__all__'
        
class PedidoVendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.PedidoVenda
        fields = '__all__'
        
class ItensPedidoVendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        models = models.ItensPedidoVenda
        fields = '__all__'