#Libs
from django.db                  import models
from shortuuid.django_fields    import ShortUUIDField
from django.utils               import timezone
from django.utils.safestring    import mark_safe

# Imports
from apps.userauth.models import User


def produt_directory_path(instance,filename):
    return 'produtos/produto_{0}/{1}'.format(instance.pid,filename)

def vendedor_directory_path(instance,filename):
    return 'vendedores/vendedor_{0}/{1}'.format(instance.vid,filename)

def marca_directory_path(instance,filename):
    return 'marcas/marca_{0}/{1}'.format(instance.mid,filename)

class Marca(models.Model):
    mid = ShortUUIDField(unique=True,length=4,max_length=10,prefix='mid',alphabet='1234567890')
    title = models.CharField(max_length=100)
    descricao = models.TextField(blank=True,null=True,default="")
    imagem = models.ImageField(upload_to=marca_directory_path,blank=True,null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(blank=True,null=True)

    class Meta:
        verbose_name_plural = "Marcas"

    def get_marca_imagem(self):
        img_url = '/media/not_found.jpg'
    
        if self.imagem:
            img_url = self.imagem.url

        return mark_safe('<img  src="%s" width="30" height="30"/>' % img_url)
    
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

class Produto(models.Model):
    pid             = ShortUUIDField(unique=True,length=10,max_length=20,prefix="prt",alphabet="abcdefgh1234567")
    cbr             = ShortUUIDField(length=4,max_length=10,prefix="cbr",alphabet="1234567890")
    
    user            = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    categoria       = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    title           = models.CharField(max_length=100)
    image           = models.ImageField(upload_to='produto',null=True,blank=True)
    descricao       = models.TextField(null=True,blank=True,default="")
    
    preco           = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    preco_antigo    = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    
    especificacao   = models.TextField(null=True,blank=True)
    tags            = models.ManyToManyField(Tags)
    
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


class ProdutoImagens(models.Model):
    imagens = models.ImageField(upload_to=produt_directory_path,blank=True,null=True)
    produto = models.ForeignKey(Produto,on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Imagens Produtos'



class Cliente(models.Model):
    cid             = ShortUUIDField(unique=True,length=10,max_length=20,prefix='cli',alphabet='abcdefgh1234567')
    user            = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    
    categoria       = models.ManyToManyField(Categoria)
    marcas          = models.ManyToManyField(Marca)
    
    endereco        = models.CharField(max_length=100)
    cep             = models.CharField(max_length=20)
    municipio       = models.CharField(max_length=100)
    estado          = models.CharField(max_length=2)
    telefone        = models.CharField(max_length=20)
    
    nacional        = models.BooleanField(default=True)
    cgc             = models.CharField(max_length=30)
    
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Clientes"

    def save(self,*args,**kwargs):
        self.updated_at = timezone.now()
        super(Cliente,self).save(*args, **kwargs)


class Vendedor(models.Model):
    vid         = ShortUUIDField(unique=True,length=10,max_length=20,prefix='vid',alphabet='abcdefgh1234567')
    
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    marcas      = models.ManyToManyField(Marca)
    clientes    = models.ManyToManyField(Cliente,related_name='clientes')
    
    endereco        = models.CharField(max_length=100,default='')
    cep             = models.CharField(max_length=20,default='')
    municipio       = models.CharField(max_length=100,default='')
    estado          = models.CharField(max_length=2,default='')
    telefone        = models.CharField(max_length=20,default='')
    
    nacional        = models.BooleanField(default=True)
    cgc             = models.CharField(max_length=30,default='')
    
    created_at      = models.DateTimeField(auto_now=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vendedores"

    def __str__(self):
        return self.nome
    

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

    pvid            = ShortUUIDField(unique=True,length=10,max_length=20,prefix="pv",alphabet="abcdefgh1234567")
    user            = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    cliente         = models.ForeignKey(Cliente,on_delete=models.SET_NULL,null=True,related_name='cliente')
    valor_total     = models.DecimalField(max_digits=9999999999, decimal_places=2,default=0)
    pago            = models.BooleanField(default=False)
    status_pedido   = models.CharField(choices=STATUS_PEDIDO_CHOICE,default=1,max_length=1)
    
    created_at      = models.DateTimeField(auto_now=True)

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

    pvid            = models.ForeignKey(PedidoVenda,on_delete=models.CASCADE,related_name='itens',null=True,blank=True)
    item            = models.CharField(max_length=4,default="0000")
    produto         = models.ForeignKey(Produto,on_delete=models.SET_NULL,null=True,related_name='produto')
    qtd             = models.DecimalField(default=0,decimal_places=2,max_digits=999999)
    status_produto  = models.CharField(choices=STATUS_PRODUTO_CHOICE,default=1,max_length=1)
    preco           = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    preco_total     = models.DecimalField(max_digits=9999999999999, decimal_places=2, default="0.00")
    
    class Meta:
        verbose_name_plural = 'Itens dos Pedido de venda'
    
    def __str__(self):
        return self.item