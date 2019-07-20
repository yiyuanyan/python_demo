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



def proxy_view(request):
    # blacklist = Person.get_blacklist()
    # for person in blacklist:
    #     print(person.username)
    return HttpResponse('Proxy')
def my_authenticate(telephone,password):
    user = User.objects.filter(extension__telephone=telephone).first()
    if user:
        is_correct = user.check_password(password)
        if is_correct:
            return user
        else:
            return None
    else:
        return None
def one_view(request):
    # user = User.objects.create_user(username='yiyuanyan1', email='asdfasdfasdf@123.com', password='111111')
    # user = User.objects.create_user(username='带有手机号码',email='sdfggggg@123.com', password='222222')
    # user.extension.telephone = '13800138000'
    # user.save()
    telephone = request.GET.get('telephone')
    password = request.GET.get('password')
    user = my_authenticate(telephone=telephone, password=password)
    if user:
        print('验证成功：%s' % user.username)
    else:
        print('验证失败')
    return HttpResponse('一对一扩展User模型')