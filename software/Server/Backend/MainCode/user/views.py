from django.shortcuts import render

# Create your views here.

# # 导入模块
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout

def login(request):
	if request.method == 'GET':
		return render(
			request,
			'html/index.html',
		)
	
	elif request.method == 'POST':
		# 获取参数
		user_name = request.POST.get('username', '')
		pwd = request.POST.get('password', '')
		
		# 用户已存在
		if User.objects.filter(username=user_name):
			# 使用内置方法验证
			user = authenticate(username=user_name, password=pwd)
			
			# 验证通过
			if user:
				# 用户已激活
				if user.is_active:
					return JsonResponse({
						'code': 200,
						'msg': '登录成功'
					})
				# 未激活
				else:
					return JsonResponse({
						'code': 200,
						'msg': '用户未激活'
					})
			
			# 验证失败
			else:
				return JsonResponse({
					'code': 403,
					'msg': '用户认证失败'
				})
		
		# 用户不存在
		else:
			return redirect('/basic/register')


