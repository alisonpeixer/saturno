#Libs
from rest_framework import serializers

# serializers.py
from dj_rest_auth.serializers import UserDetailsSerializer



# Models
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields= ['pk','email','first_name','last_name','username','user_image','password','image']
        extra_kwargs = {
            'password': {'write_only': True,'required':False},
            'email': {'write_only': False,'required':False}
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
        instance.image = validated_data.get('image', instance.image)
        instance.first_name = validated_data.get('first_name', instance.first_name).upper()
        instance.last_name = validated_data.get('last_name', instance.last_name).upper()

        instance.save()
        return instance
              
                 


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = User
        fields = ['pk','email','first_name','last_name','username','password','image']
        extra_kwargs = {
            'password': {'write_only': True,'required':False},
            'email': {'write_only': False,'required':False}
        }

