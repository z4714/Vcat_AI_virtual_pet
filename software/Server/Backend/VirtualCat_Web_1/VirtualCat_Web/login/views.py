from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Account, Email, UserInfo
from django.http import JsonResponse
from django.views import View
import json
#from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login, logout
import smtplib #用于邮件的发信动作
from email.mime.text import MIMEText #用于构建邮件内容
from email.header import Header #用于构建邮件头
from django.db import IntegrityError
import random
from datetime import date


#发信服务器
smtp_server = 'smtp.qq.com'
#发信方的信息：发信邮箱，授权码
from_addr = '1712968536@qq.com'
stmpcode = 'xculhadcpahkdjij'
#收信方邮箱
to_addr = ''

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
                            'avatar':user_info.avatar if user_info.avatar else None,
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
                            'avatar':corr_pwd.avatar if corr_pwd.avatar else None,
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
                            'username': corr_pwd.uname,#account
                            'email': corr_email.email,
                            'nickname':corr_pwd.nickname,
                            'gender':corr_pwd.gender,
                            'birth':corr_pwd.birth,
                            'date':corr_pwd.date,
                            'avatar':corr_pwd.avatar if corr_pwd.avatar else None,
                        }
                    })

            return JsonResponse({'code': 400, 'message': "登录失败,没找到用户信息"}, status=400)


class LogoutView(View):
    # 退出登录
    def get(self, request):
        logout(request)
        return JsonResponse({'code': 200, 'message': "已注销用户登录"})

class RegisterView(View):

    def post(self,request):
        
        params = request.POST if len(request.POST) else json.loads(request.body.decode())

        if(params.get('email')):
            email = params.get('email') 
            email_exist = Email.objects.filter(email=email).first()
            if email_exist:
                return JsonResponse({'code': 400, 'message': "邮箱已被注册"})

            
            to_addr = email
            print(email+"\n")
            #生成验证码 
            rand_captcha = random.randint(100000, 999999)
            request.session['rand_captcha'] = rand_captcha

            #邮箱正文内容，第一个参数为内容，第二个为格式（plain：纯文本），第三编码
            msg = MIMEText(f'Vcat注册验证码:{rand_captcha}','plain','utf-8')
            #邮件头
            msg['From']=Header(from_addr)
            msg['To']=Header(to_addr)
            server = smtplib.SMTP_SSL(host='smtp.qq.com')
            server.connect(host='smtp.qq.com',port=465)
            server.login(from_addr, stmpcode)
            server.sendmail(from_addr, to_addr, msg.as_string())
            server.quit()
            return JsonResponse({'code': 200, 'message': "已发送验证码到邮箱"})
        elif params.get('captcha'):
            
            user_captcha = params.get('captcha')
            rand_captcha = request.session.get('rand_captcha')
            print(str(user_captcha) + "\n" + str(rand_captcha) + "\n")
            if rand_captcha and user_captcha == str(rand_captcha):
                # 验证码匹配，邮箱可用
                return JsonResponse({'code': 200, 'message': "邮箱验证通过"})
            else:
                return JsonResponse({'code': 400, 'message': "验证码错误"})
        
        return JsonResponse({'code': 400, 'message': "请求参数错误"})


class RegistUserInfoView(View):
    def post(self,request):
        #此接口默认对应网页端的注册行为，所以默认account使用的都是email
        #（默认用户都用email进行注册）
        params = request.POST if len(request.POST) else json.loads(request.body.decode())
        account = params.get('account')
        print(account)
        if not account:
            return JsonResponse({'code': 400, 'message': "账号不能为空"})
        try:
            ruser_info = UserInfo(
                uname=account,
                pwd = params.get('password'),
                nickname = params.get('nickname'),
                gender = params.get('gender'),
                birth = params.get('birth'),
                date = date.today(),
                avatar = params.get('avatar')
            )
            ruser_info.save()#录入注册信息
        
            remail = Email( email=params.get('account'))
            remail.save() #对应邮箱信息到uid

            raccount =Account(uname = params.get('account'))
            raccount.save()#对应账户信息到uid

            return JsonResponse({'code': 200, 'message': "用户注册成功"})
        except IntegrityError as e:
                        return JsonResponse({'code': 400, 'message': "保存数据失败: " + str(e)})

def index(request):
    print("进入 index")
    return render(request, 'static/html/index.html')
