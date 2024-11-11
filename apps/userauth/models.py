# Libs
from django.db                  import models
from django.contrib.auth.models import AbstractUser
from django.utils               import timezone
from django.utils.safestring    import mark_safe
from shortuuid.django_fields    import ShortUUIDField

import os


def user_directory_path(instance,filename):
    return 'users/user_{0}/{1}'.format(instance.uid,filename)

# User
class User(AbstractUser): 
    uid = ShortUUIDField(length=10,max_length=20,prefix='uid',alphabet='abc1234567')
    
    TIPO_USUARIO_CHOICES = (
        ('S','Staff'),
        ('V','Vendedor'),
        ('C','Cliente'),
    )
    
    email           = models.EmailField(unique=True)
    tipo_usuario    = models.CharField(choices=TIPO_USUARIO_CHOICES,max_length=1,default='C')
    
    username        = models.CharField(max_length=40)
    image           = models.ImageField(upload_to=user_directory_path, default='/user_default/user_default.png', blank=True,null=True)
    
    updated_at      = models.DateTimeField(null=True,blank=True)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name_plural = "Users"


    def get_user_image(self):
        url_img = '/media/users/user_default/user_default.png'
        
        if self.image and hasattr(self.image, 'url'):
            url_img = self.image.url
                       
        return mark_safe('<img src="%s" width="30" height="30"/>' % url_img)

    def user_image(self):
        
        if self.image and hasattr(self.image, 'url') :
            return self.image.url
        
        return '/media/users/user_default/user_default.png'
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()

        if not self.image:
            self.image = 'users/user_default/user_default.png'
        
        super(User, self).save(*args, **kwargs)