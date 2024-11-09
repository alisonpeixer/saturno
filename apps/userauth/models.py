from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.safestring import mark_safe

def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.id,filename)

# User
class User(AbstractUser): 
    email       = models.EmailField(unique=True)
    username    = models.CharField(max_length=40)
    image       = models.ImageField(upload_to=user_directory_path, default='')
    
    updated_at  = models.DateTimeField(null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name_plural = "Users"
        
    def user_image(self):
        return mark_safe('<img src="%s" width="30" height="30"/>' % self.image.url)
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        if self.pk:
            self.updated_at = timezone.now()

        super(User, self).save(*args, **kwargs)