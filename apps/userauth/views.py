#Libs
from rest_framework  import status
from rest_framework.response import Response
from rest_framework import viewsets, views

#Models
from .models import  User

#Serializers
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class UserCreateView(views.APIView):
    authentication_classes  = []
    permission_classes      = []
    
    def post(self,request,*args,**kwargs):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({"mensage": 'OK'},status=status.HTTP_200_OK)
        
        return Response({"menssage": serializer.errors},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    