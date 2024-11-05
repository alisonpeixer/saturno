#Libs
from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Imports
from apps.userauth.models import User


class Categoria(models.Model):
    cId     = ShortUUIDField(unique=True,length=10,max_length=20,prefix="ctg",alphabet="abcdefgh1234567")
    title   = models.CharField(max_length=100)
    image   = models.ImageField(upload_to='categoria')
    
    class Meta:
        verbose_name_plural = "Categorias"
        
    def categoria_image(self):
        return self.image.url

    def __str__(self):
        return self.title

class Tags(models.Model):
    pass

class Produto(models.Model):
    pId         = ShortUUIDField(unique=True,length=10,max_length=20,prefix="prt",alphabet="abcdefgh1234567")
    sku         = ShortUUIDField(unique=True,length=4,max_length=10,prefix="sku",alphabet="1234567890")
    
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria   = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    
    
    title       = models.CharField(max_length=100)
    image       = models.ImageField(upload_to='produto')
    descricao   = models.TextField(null=True,blank=True,default="")
    
    preco       = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    preco_antigo    = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    
    especificacao   = models.TextField(null=True,blank=True)
    tags            = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True,blank=True)
    
    class Meta:
        verbose_name_plural = "Produtos"
        
    def produto_image(self):
        return self.image.url

    def __str__(self):
        return self.title
    
    