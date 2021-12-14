from django.db import models
import time
import datetime
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.http import HttpResponse, JsonResponse
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def jsonRes(msg, status,context=False):
    if context == False:
        return {
            'msg': msg,
            'status': status,
        }
    else :
        return {
            'msg': msg,
            'status': status,
            'context':context,
        }


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(
            username=username.lower(),
            email=self.normalize_email(email),
            **extra_fields)
        # user name is converted into lowercase
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.create_user(
            username, email
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class Userinfo(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, default=0)
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    @staticmethod
    def check_ex(username):
        user = Userinfo.objects.get(username=username)
        print(user)

    def reg_check_p(self, p1, p2):
        if p1 != p2:
            return jsonRes('密码不一样', 1)
        elif len(p1) < 8:
            print(len(p1))
            return jsonRes('密码长度过短', 2)
        else:
            return jsonRes('注册成功', 3)

    def log_check_p(self, p):
        if self.password != p:
            return jsonRes('密码错误', 1)
        else:
            return jsonRes('登录成功', 2)

    def check_e(self):
        pass

    # def check_u(self,username):
    #     try :
    #         user = Userinfo.objects.get(username=username)
    #     except :
    #         return jsonRes('没有该用户',3)
    #     return True

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

# class Userinfo(models.Model):
#     username = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     email = models.CharField(max_length=20)
#     is_anonymous = models.BooleanField()
#     is_authenticated = models.BooleanField()
#
#     REQUIRED_FIELDS = ["username", "password", "email"]
#     USERNAME_FIELD = "id"
#
#     class Meta:
#         verbose_name_plural = "Userinfo"

#
class Tasks(models.Model):
    uid = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    # deadline = models.DateTimeField(max_length=20)

    def to_dict(self):
        obj = {
            "id": self.id,
            'title':self.title,
            "content": self.content,
            "created_time": self.created_time
        }
        return obj

    class Meta:
        verbose_name_plural = "Tasks"
