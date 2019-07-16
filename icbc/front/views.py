from django.shortcuts import render, redirect, reverse
from .models import User
from django.views.generic import View
from .forms import RegisterForm
from .models import User
# Create your views here.
def index(request):
    return render(request, 'index.html')


#  登陆
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        pass


#  注册
class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create(email=email, password=password, username=username, balance=1000)


#  转账
class TransferView(View):
    def get(self, request):
        return render(request, 'transfer.html')

    def post(self, request):
        pass
