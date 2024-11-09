#Libs
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils import timezone

# Imports
from apps.userauth.models import User


def produt_directory_path(instance,filename):
    return 'produto_{0}/{1}'.format(instance.pid,filename)

def vendedor_directory_path(instance,filename):
    return 'vendedor_{0}/{1}'.format(instance.vid,filename)

def marca_directory_path(instance,filename):
    return 'marca_{0}/{1}'.format(instance.mid,filename)

class Marca(models.Model):
    mid = ShortUUIDField(unique=True,length=4,max_length=4,prefix='mid',alphabet='1234567890')
    title = models.CharField(max_length=100)
    descricao = models.TextField(blank=True,null=True,default="")
    imagem = models.ImageField(upload_to=marca_directory_path,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "Marcas"

    def marca_imagem(self):
        return self.imagem.url
    
    def __str__(self):
        return self.title

    def save(self, *args,**kwargs):
        self.updated_at = timezone.now()

        super(Marca, self).save(*args,**kwargs)

class Categoria(models.Model):
    cid     = ShortUUIDField(unique=True,length=10,max_length=20,prefix="ctg",alphabet='abcdefgh1234567')
    title   = models.CharField(max_length=100)
    image   = models.ImageField(upload_to='categoria')
    
    class Meta:
        verbose_name_plural = "Categorias"
        
    def categoria_image(self):
        return self.image.url

    def __str__(self):
        return self.title

class Tags(models.Model):
    tid = ShortUUIDField(unique=True,length=10,max_length=20,prefix="teg",alphabet='abcdefgh1234567')
    title = models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title

class Vendedor(models.Model):
    vid = ShortUUIDField(unique=True,length=10,max_length=20,prefix='vid',alphabet='abcdefgh1234567')
    nome = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    marcas = models.ForeignKey(Marca, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.nome

class Produto(models.Model):
    pid             = ShortUUIDField(unique=True,length=10,max_length=20,prefix="prt",alphabet="abcdefgh1234567")
    cbr             = ShortUUIDField(length=4,max_length=10,prefix="cbr",alphabet="1234567890")
    
    user            = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria       = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    title           = models.CharField(max_length=100)
    image           = models.ImageField(upload_to='produto')
    descricao       = models.TextField(null=True,blank=True,default="")
    
    preco           = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    preco_antigo    = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    
    especificacao   = models.TextField(null=True,blank=True)
    tags            = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(null=True,blank=True)


    class Meta:
        verbose_name_plural = "Produtos"
        
    def produto_image(self):
        return self.image.url

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.pk:
            odlItem = Produto.objects.get(pk=self.pk)
            self.preco_antigo = odlItem.preco

        self.updated_at = timezone.now()
        super(Produto, self).save(*args, **kwargs)


class ProdutosImagens(models.Model):
    imagens = models.ImageField(upload_to=produt_directory_path,blank=True,null=True)
    produto = models.ForeignKey(Produto,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Imagens Produtos'



# ==================================== PEDIDO DE VENDA ===================================================== #

class PedidoVenda(models.Model):
    STATUS_PEDIDO_CHOICE = (
       (1,'Pendente'),
       (2,'Processando'),
       (3,'Aguardando Pagamento'),
       (4,'Pagamento Realizado'),
       (5,'Em Separação'),
       (6,'Aguardando a Coleta'),
       (7,'Em Transporte'),
       (8,'Entregue'),
       (9,'Finalizado'),
       (0,'Cancelado')
    )

    pvid = ShortUUIDField(unique=True,length=10,max_length=20,prefix="pv",alphabet="abcdefgh1234567")
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    valor_total = models.DecimalField(max_digits=9999999999, decimal_places=2,default=0)
    pago = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    status_pedido = models.CharField(choices=STATUS_PEDIDO_CHOICE,default=1,max_length=1)

    class Meta:
        verbose_name_plural = 'Pedidos de Venda'
    
    def __str__(self):
        return self.pvid

class ItensPedidoVenda(models.Model):
    STATUS_PRODUTO_CHOICE = (
        (1,'Não Informado'),
        (2,'Em Estoque'),
        (3,'Sem Estoque'),
        (4,'Em Producao'),
        (5,'Fora de Linha')
    )

    pvid = models.ForeignKey(PedidoVenda,on_delete=models.CASCADE)
    item = models.CharField(max_length=4,default="0000")
    produto = models.ForeignKey(Produto,on_delete=models.SET_NULL,null=True)
    qtd = models.DecimalField(default=0,decimal_places=2,max_digits=999999)
    status_produto = models.CharField(choices=STATUS_PRODUTO_CHOICE,default=1,max_length=1)
    preco           = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    preco_total =     models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    
    class Meta:
        verbose_name_plural = 'Itens dos Pedidos de venda'
    
    def __str__(self):
        return self.item