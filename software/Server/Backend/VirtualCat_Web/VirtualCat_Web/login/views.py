from django.shortcuts import render,HttpResponse,redirect,reverse
from .models import Accounts
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import AccountSerializer
# Create your views here.


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

def login(request):

    if request.method == 'POST':
        print("进入页面")
        email = request.POST['username']
        password = request.POST['password']
        corr_email = Accounts.objects.filter(email=email).first()
        print("获取到信息")
        if email == corr_email.email and password == corr_email.password:
            print('登录成功')
            return HttpResponse('登录成功')

    return render(request,'./static/html/main.html')

def logon(request):
    return HttpResponse('留作练习')

def logout(request):
    return HttpResponse('退出')

def index(request):
   print("进入index")
   return render(request, 'static/html/index.html')
