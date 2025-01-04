#Libs
from rest_framework import status
from rest_framework import viewsets,permissions
from rest_framework.response import Response
from django.core.files.uploadedfile import SimpleUploadedFile
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from decimal import Decimal

#Models
from apps.core import models

#Serializers
from apps.core import serializers




class ProdutoViews(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields    = ['title','descricao','cbr','descricao']
    search_fields       = ['title','descricao','cbr','descricao']
    
    def perform_create(self, serializer): 
        serializer.save(user=self.request.user) # gravando o usuario da inclusao
        
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tags = serializer.validated_data.pop('tags', [])


        produto = models.Produto.objects.create(**serializer.validated_data)

        produto.tags.set(tags)
        

        for img_data in request.FILES.getlist('produto_imagens'):
            if img_data.content_type == "image/webp":
                # Lê o conteúdo como bytes
                webp_bytes = img_data.read()

                # Cria um arquivo em memória com SimpleUploadedFile
                img_file = SimpleUploadedFile(
                    name=img_data.name,
                    content=webp_bytes,
                    content_type="image/webp"
                )
            
            models.ProdutoImagens.objects.create(produto=produto, imagen=img_data)

        return Response(serializer.to_representation(produto), status=status.HTTP_201_CREATED)



class ProdutoImagensViews(viewsets.ModelViewSet):
    queryset = models.ProdutoImagens.objects.all()
    serializer_class = serializers.ProdutoImagensSerializer  # Use o serializer correto aqui
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]


class MarcaViews(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]


class CategoriaViews(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]


class TagsViews(viewsets.ModelViewSet):
    queryset = models.Tags.objects.all()
    serializer_class = serializers.TagsSerializer
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
   
            
class ClienteViews(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
  

class VendedorViews(viewsets.ModelViewSet):
    queryset = models.Vendedor.objects.all()
    serializer_class = serializers.VendedorSerializer
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
   

class PedidoVendaViews(viewsets.ModelViewSet):
    queryset = models.PedidoVenda.objects.all()
    serializer_class = serializers.PedidoVendaSerializer

    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]
    
    def get_queryset(self):
        return models.PedidoVenda.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        request.data['user'] = self.request.user.id
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        itens_data = request.data.pop('itens')

        pedido = self.perform_create(serializer)

        # Cria os itens do pedido
        item = 1
        for item_data in itens_data:
            produto = item_data.get('produto') 
            try:
                produto = models.Produto.objects.get(id=produto['id'])
            except models.Produto.DoesNotExist:
                return Response({"detail": "Produto não encontrado."}, status=status.HTTP_404_NOT_FOUND)
            
            item_data['produto'] = produto
            item_data['pvid'] = pedido
            item_data['item'] = f"{item:04}"
            item_data['preco'] = produto.preco
            item_data['preco_total'] = produto.preco * Decimal(item_data['qtd'])  # Certifique-se de que a quantidade seja numérica

            item_data.pop('crid', None)
            item_data.pop('created_at', None)
            item_data.pop('user', None)

            models.ItensPedidoVenda.objects.create(**item_data)
            item += 1
            pedido.valor_total += item_data['preco_total']

        pedido.save()

        return Response(serializer.to_representation(pedido), status=status.HTTP_201_CREATED)
        
class ItensPedidoVendaViews(viewsets.ModelViewSet):
    queryset = models.ItensPedidoVenda.objects.all()
    serializer_class = serializers.ItensPedidoVendaSerializer
   
   
class CarrinhoViews(viewsets.ModelViewSet):
    queryset = models.Carrinho.objects.all()
    serializer_class = serializers.CarrinhoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    filter_backends     = [DjangoFilterBackend, filters.SearchFilter]

    def get_queryset(self):
        return models.Carrinho.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        produto_id = self.request.data['produto']
        produto = models.Produto.objects.get(pk=produto_id)
        user = self.request.user

        carrinho_item = models.Carrinho.objects.filter(user=user, produto=produto).first()

        if carrinho_item:
            carrinho_item.qtd += int(self.request.data['qtd'])
            carrinho_item.save()
        else:
            serializer.save(user=user, produto=produto)