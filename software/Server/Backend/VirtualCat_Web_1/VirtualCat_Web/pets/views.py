from sqlite3 import IntegrityError
from django.shortcuts import render
from django.views import View
from .models import PetsInfo
from django.http import JsonResponse
import json
from datetime import date

# Create your views here.



class CabinView(View):
    
    #宠物仓接口
    def post(self,request):
        #权限管理
        #print(request.session['user_id'])
        params = request.POSt if len(request.POST) else json.loads(request.body.decode())
        if 'uid' not in request.session or params.get('uid')!=request.session['uid']:
            # 用户未登录，返回未授权的错误信息
            return JsonResponse({'code': 401, 'message': "未授权"}, status=401)
        '''获取宠物列表'''
        uid = request.session['uid']
        petsInfo = PetsInfo.objects.all()
        petcabin = []
        for p in petsInfo:
            dict = {"pet_id":p.pet_id,"pet_name":p.pet_name,"description":p.description,"p_avatar":p.p_avatar}
            petcabin.append(dict)
        return JsonResponse({'code':200, 'message': "获取成功","petcabin":petcabin})


        

    def delete(self,request):
        '''删除宠物'''


class AddPetView(View):
    

    def post(self,request):
        '''添加及其他操作'''
        if 'uid' not in request.session:
            # 用户未登录，返回未授权的错误信息
            return JsonResponse({'code': 401, 'message': "未授权"}, status=401)
        params = request.POST if len(request.POST) else json.loads(request.body.decode())
        uid = request.session['uid']

        try:
            pet_info = PetsInfo(
                pet_name = params.get('pet_name'),
                pet_type = params.get('pet_type'),
                gender = params.get('gender'),
                description = params.get('description'),
                mode_type = params.get('mode_type'),
                uid = request.session['uid'],
                date = date.today(),
                p_avatar = params.get('p_avatar')
                


            )
            pet_info.save()#录入注册信息
            return JsonResponse({'code':200, 'message': "添加成功"})
        except IntegrityError as e:
            return JsonResponse({'code': 400, 'message': "保存数据失败: " + str(e)})
        

    def delete(self,request):
        '''删除宠物'''