# Libs
from django.contrib import admin

# Models
from .models import Produto, Categoria, Tags, Marca, Vendedor, ProdutosImagens, PedidoVenda, ItensPedidoVenda


class ProdutoAdmin(admin.ModelAdmin):
  list_display = ['pid','title','descricao','preco']

class CategoriaAdmin(admin.ModelAdmin):
  list_display = ['cid','title']

class TagsAdmin(admin.ModelAdmin):
  list_display = ['tid', 'title']


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(Vendedor)
admin.site.register(Marca)
admin.site.register(ProdutosImagens)

admin.site.register(PedidoVenda),
admin.site.register(ItensPedidoVenda)