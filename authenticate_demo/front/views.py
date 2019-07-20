from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.

def index(request):
    # user = User.objects.create_user(username='yiyuanyan', email='yiyuanhanly@126.com', password='Hejianxin88')
    # user = User.objects.create_superuser(username='hjx', email='yiyuanyan@126.com', password='Hejianxin88')
    username = 'hjx'
    password = '123456'
    user = authenticate(request, username=username, password=password)
    if user:
        print('登录成功:%s' % user.username)
    else:
        print('用户名或密码错误')


    return HttpResponse("success")

