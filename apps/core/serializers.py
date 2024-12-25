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
    produto_imagens = ProdutoImagensSerializer(many=True, required=False)
    
    class Meta:
        model = models.Produto
        fields = '__all__'

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])  
        produto_imagens_data = self.initial_data.pop('produto_imagens', [])

        produto = models.Produto.objects.create(**validated_data)

        produto.tags.set(tags)  

        for img_data in produto_imagens_data:
            models.ProdutoImagens.objects.create(produto=produto, imagen=img_data)

        return produto



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
    itens = ItensPedidoVendaSerializer(many=True)

    class Meta:
        model = models.PedidoVenda
        fields = '__all__'

    def create(self, validated_data):
        itens_data = validated_data.pop('itens')
        pedido = models.PedidoVenda.objects.create(**validated_data)
        
        # Salva os itens do pedido
        item = 1
        for item_data in itens_data:
            item_data['pvid'] = pedido
            item_data['item'] = f"{item:04}"
            models.ItensPedidoVenda.objects.create(**item_data)
            item += 1
        return pedido