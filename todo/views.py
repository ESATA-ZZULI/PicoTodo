from django.shortcuts import render, HttpResponse
from . import models
from django.http import HttpResponse, JsonResponse
from .models import Userinfo, Tasks


# Create your views here.

def jsonRes(msg, status):
    return {
        'msg': msg,
        'status': status
    }


def index(request):
    return HttpResponse('这是主页')

def fuck():
    def login_todo(request):
        if request.method == 'GET':
            user_data = request.GET['user_data']
            username = user_data['username']
            password1 = user_data['password1']
            password2 = user_data['password2']
            if password2 and password1 and password1 != password2:
                context = {'msg': '两次密码不同', 'status': '0'}
                return JsonResponse(context)
            all_user = models.Userinfo.objects.get()
            flag = 0
            user = user_data
            for i in all_user:
                if username == i.username:
                    flag = 1
                    user = i
                    break
            if flag == 0:
                context = jsonRes('没有该用户', 1)
                return JsonResponse(context)
            else:
                if password1 == user.password:
                    context = {'msg': '登录成功', 'status': '2'}
                    return JsonResponse(context)
                else:
                    context = {'msg': '密码错误', 'status': '3'}
                    return JsonResponse(context)
