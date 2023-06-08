from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Account, Email, UserInfo
from django.http import JsonResponse
from django.views import View
import json
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login, logout


# 登录接口定义视图
class LoginView(View):

    def post(self, request):
        # 处理 POST 请求
        params = request.POST if len(request.POST) else json.loads(request.body.decode())
        account = params.get('account')
        password = params.get('password')
        print(account+"\n"+password)


        if account.isnumeric():
            # 账号是一个数字，按 uid 匹配
            corr_id = Account.objects.filter(uid=int(account)).first()
            if corr_id:
                # 找到匹配的账号
                # 进一步处理密码验证逻辑

                if password == corr_id.password:
                    request.session['user_id'] = corr_id.uid
                    user_info = UserInfo.objects.get(uname=corr_id.uname)
                    email = Email.objects.get(uid=corr_id.uid)
                    return JsonResponse({'code': 200, 'message': "登录成功",
                        'UserInfo': {
                            'uid':email.uid,
                            'username': user_info.uname,
                            'email': email.email,
                            'nickname':user_info.nickname,
                            'gender':user_info.gender,
                            'birth':user_info.birth,
                            'date':user_info.date,
                            'photo':user_info.photo.url if user_info.photo else None,
                        }
                    })
                else:
                    return JsonResponse({'code': 400, 'message': "密码错误"})
            else:
                return JsonResponse({'code': 400, 'message': "账号不存在"})
        else:
            # 账号不是一个数字，按 email 或 uname 匹配
            corr_email = Email.objects.filter(email=account).first()
            corr_username = Account.objects.filter(uname=account).first()

            if corr_email:
                # 账号匹配到了 email 字段
                username = corr_email.uid
                username = Account.objects.filter(uid=username).first()
                username = username.uname
                corr_pwd = UserInfo.objects.filter(uname=username).first()
                if password == corr_pwd.pwd:
                    # 登录成功，将用户信息存储到会话中
                    request.session['user_id'] = corr_email.uid
                    return JsonResponse({
                        'code': 200,
                        'message': "登录成功",
                         'UserInfo': {
                            'uid':corr_email.uid,
                            'username': corr_pwd.uname,
                            'email': corr_email.email,
                            'nickname':corr_pwd.nickname,
                            'gender':corr_pwd.gender,
                            'birth':corr_pwd.birth,
                            'date':corr_pwd.date,
                            'photo':corr_pwd.photo.url if corr_pwd.photo else None,
                        }
                    })
            elif corr_username:
                # 账号匹配到了 uname 字段
                corr_pwd = UserInfo.objects.filter(uname=account).first()
                
                corr_email = Email.objects.filter(uid=corr_username.uid).first()
                if password == corr_pwd.pwd:
                    # 登录成功，将用户信息存储到会话中
                    request.session['user_id'] = corr_username.uid
                    return JsonResponse({
                        'code': 200,
                        'message': "登录成功",
                         'UserInfo': {
                            'uid':corr_username.uid,
                            'username': corr_pwd.uname,
                            'email': corr_email.email,
                            'nickname':corr_pwd.nickname,
                            'gender':corr_pwd.gender,
                            'birth':corr_pwd.birth,
                            'date':corr_pwd.date,
                            'photo':corr_pwd.photo.url if corr_pwd.photo else None,
                        }
                    })

            return JsonResponse({'code': 400, 'message': "登录失败"}, status=400)


class LogoutView(View):
    # 退出登录
    def get(self, request):
        logout(request)
        return JsonResponse({'code': 200, 'message': "已注销用户登录"})


def index(request):
    print("进入 index")
    return render(request, 'static/html/index.html')
