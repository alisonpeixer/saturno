from django.db import models
from django.contrib.auth.models import AbstractUser



def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.id,filename)

# User
class User(AbstractUser): 
    email       = models.EmailField(unique=True)
    username    = models.CharField(max_length=40)
    image       = models.ImageField(upload_to=user_directory_path, default='')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name_plural = "Users"
        
    def user_image(self):
        return self.image.url
    
    def __str__(self):
        return self.username