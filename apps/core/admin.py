# Libs
from django.contrib import admin

# Models
from .models import Produto, Categoria, Tags, Marca, Vendedor, ProdutoImagens, PedidoVenda, ItensPedidoVenda, Carrinho


class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['pid','title','descricao','preco']

class CategoriaAdmin(admin.ModelAdmin):
  list_display = ['cid','title']

class TagsAdmin(admin.ModelAdmin):
  list_display = ['tid', 'title']

class MarcaAdmin(admin.ModelAdmin):
  list_display = ['mid','title','get_marca_imagem']

class CarrinhoAdmin(admin.ModelAdmin):
  list_display = ['crid','user','produto','qtd', 'created_at']
  
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Marca,MarcaAdmin)
admin.site.register(Vendedor)
admin.site.register(ProdutoImagens)

admin.site.register(PedidoVenda),
admin.site.register(ItensPedidoVenda)

admin.site.register(Carrinho,CarrinhoAdmin)