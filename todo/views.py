from django.shortcuts import render, HttpResponse
from . import models
from django.http import HttpResponse, JsonResponse
from .models import Userinfo


# Create your views here.

def jsonRes(msg, status):
    return {
        'msg': msg,
        'status': status
    }


def index(request):
    return HttpResponse('这是主页')





def reg(request):
    if request.method == 'POST':
        user_data = request.POST
        username = user_data['username']
        password1 = user_data['password1']
        password2 = user_data['password2']
        try:
            obj = models.Userinfo.objects.get(username=username)
            return JsonResponse(jsonRes('该用户已注册', 0))
        except:
            pass
        user = models.Userinfo(username=username)
        context = user.reg_check_p(password1, password2)
        if context['status'] == 3:
            user.save()
        return JsonResponse(context)


def log(request):
    if request.method == 'POST':
        user_data = request.POST
        username = user_data['username']
        password = user_data['password']
        user = models.Userinfo()
        try:
            models.Userinfo.check_ex(username)
            # obj = models.Userinfo.objects.get(username=username)
        except:
            return JsonResponse(jsonRes('没有该用户', 0))
        context = user.log_check_p(password)
    return JsonResponse(context)
