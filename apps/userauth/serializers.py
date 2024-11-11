#Libs
from rest_framework import serializers


# Models
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields= ['id','email','first_name','last_name','username','user_image','password','image']
        extra_kwargs = {
            'password': {'write_only': True,'required':False},
            'email': {'write_only': True,'required':False},
            'image': {'write_only': True},
        }
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        
        user = User(**validated_data)
        user.set_password(password)	
        
        user.save()
        
        return user
    
    
    def update(self, instance, validated_data):
        
        email = validated_data.get('email', instance.email)
        senha = validated_data.get('password',None)
        
        if senha:
            instance.set_password(senha)
            
        instance.email = email
        instance.username = validated_data.get('username', instance.username)
        instance.tipo_usuario = validated_data.get('tipo_usuario', instance.tipo_usuario)
        instance.image = validated_data.get('image', instance.image)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)

        instance.save()
        return instance
              
                 


