from django.shortcuts import render,HttpResponse,redirect,reverse
from .models import Account, Email, UserInfo
from django.http import JsonResponse
from django.views import View
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate,login,logout
# Create your views here.

#登录接口定义视图
class LoginView(View):
    
    def post(self, request):
        # 处理POST请求
        params = request.POST if len(request.POST) else json.loads(request.body.decode())
        account = params.get('account')
        password = params.get('password')

        if account.isnumeric():
            # 账号是一个数字，按uid匹配
            corr_id = Account.objects.filter(uid=int(account)).first()
            if corr_id:
                # 找到匹配的账号
                # 进一步处理密码验证逻辑
                if password == corr_id.password:
                    request.session['user_id'] = corr_id.uid
                    return JsonResponse({'code': 200, 'message': "登录成功"})
                else:
                    return JsonResponse({'code': 400, 'message': "密码错误"})
            else:
                return JsonResponse({'code': 400, 'message': "账号不存在"})
        else:
            # 账号不是一个数字，按email或uname匹配
            corr_email = Email.objects.filter(email=account).first()
            corr_username = Account.objects.filter(uname=account).first()

            if corr_email:
                # 账号匹配到了email字段
                username = corr_email.uid
                username = Account.objects.filter(uid=username).first()
                username = username.uname
                corr_pwd = UserInfo.objects.filter(uname=username).first()
                if password == corr_pwd.pwd:
                    # 登录成功，将用户信息存储到会话中
                    request.session['user_id'] = corr_email.uid
                    return JsonResponse({'code': 200, 'message': "登录成功"})
            elif corr_username:
                # 账号匹配到了uname字段
                corr_pwd = UserInfo.objects.filter(uname=account).first()
                if password == corr_pwd.pwd:
                    # 登录成功，将用户信息存储到会话中
                    request.session['user_id'] = corr_username.uid
                    return JsonResponse({'code': 200, 'message': "登录成功"})

            return JsonResponse({'code': 400, 'message': "登录失败"}, status=400)
'''
def login(request):

    if request.method == 'POST':
        print("进入页面")
        email = request.POST['username']
        password = request.POST['password']
        corr_email = Account.objects.filter(email=email).first()
        print("获取到信息")
        if email == corr_email.email and password == corr_email.password:
            print('登录成功')
            return HttpResponse('登录成功')

    return render(request,'./static/html/main.html')

def logon(request):
    return HttpResponse('')

def logout(request):
    return HttpResponse('退出')
'''


class LogoutView(View):
    #退出登录
    def get(self,request):
        logout(request)
        return JsonResponse({'code':200,'message':"已注销用户登录"})


def index(request):
   print("进入index")
   return render(request, 'static/html/index.html')
