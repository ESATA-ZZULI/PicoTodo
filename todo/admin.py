from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

# Register your models here.''''

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display=['username','email']


admin.site.register(models.Userinfo, UserAdmin)