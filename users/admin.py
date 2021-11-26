from django.db import models


# Register your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField('用户名', max_length=32, default='')
