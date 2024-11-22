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
        model = models.ProdutoImagens
        fields = '__all__'


class MarcaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Marca
        fields = '__all__'
        
class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Categoria
        fields = '__all__'
    
class TagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tags
        fields = '__all__'
            
class ClienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Cliente
        fields = '__all__'

class VendedorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Vendedor
        fields = '__all__'


class ItensPedidoVendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ItensPedidoVenda
        fields = ['pvid','item','produto','qtd','status_produto','preco','preco_total']     

class PedidoVendaSerializer(serializers.ModelSerializer):
    itens = ItensPedidoVendaSerializer(many=True)


    class Meta:
        model = models.PedidoVenda
        fields = ['id', 'pvid', 'user', 'cliente', 'valor_total', 'pago', 'status_pedido', 'itens', 'created_at']

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = models.PedidoVenda.objects.create(**validated_data)
        
        for item_data in itens_data:
            item_data['pvid'] = pedido
            models.ItensPedidoVenda.objects.create(**item_data)
        
        return pedido