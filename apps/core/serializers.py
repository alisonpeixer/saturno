#Libs
from rest_framework import serializers


#Models
from apps.core import models

class ProdutoImagensSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = models.ProdutoImagens
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tags
        fields = '__all__'
            

class ProdutoSerializer(serializers.ModelSerializer):
    tags = TagsSerializer(many=True, read_only=True)
    produto_imagens = ProdutoImagensSerializer(many=True, required=False, read_only=True)
    
    class Meta:
        model = models.Produto
        fields = '__all__'



class MarcaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Marca
        fields = '__all__'
        
class CategoriaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Categoria
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
        fields = '__all__'

class PedidoVendaSerializer(serializers.ModelSerializer):
    itens = ItensPedidoVendaSerializer(many=True,read_only=True)

    class Meta:
        model = models.PedidoVenda
        fields = '__all__'
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['desc_status_pedido'] = instance.get_status_pedido_display()
        return rep
    
        
class CarrinhoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)  # pegando os dados do produto

    class Meta:
        model = models.Carrinho
        fields = '__all__'
    

        