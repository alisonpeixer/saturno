#Libs
from rest_framework import viewsets


#Models
from apps.core import models

#Serializers
from apps.core import serializers



class ProdutoViews(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    
    def perform_create(self, serializer): 
        #Gravando o usuario da inclusao
        serializer.save(user=self.request.user)