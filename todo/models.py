from django.db import models
import time
import datetime


# Create your models here.
class Userinfo(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    is_anonymous = models.BooleanField()
    is_authenticated = models.BooleanField()

    REQUIRED_FIELDS = ["username", "password", "email"]
    USERNAME_FIELD = "id"

    class Meta:
        verbose_name_plural = "Userinfo"


class Tasks(models.Model):
    uid = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=20)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(max_length=20)

    class Meta:
        verbose_name_plural = "Tasks"
