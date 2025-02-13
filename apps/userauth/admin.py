from django.contrib import admin

from .models import User

# Custom User Model
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','get_user_image']

admin.site.register(User,UserAdmin)