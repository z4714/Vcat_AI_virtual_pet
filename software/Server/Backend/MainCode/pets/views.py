from django.shortcuts import render
from django.views import View
from .models import PetsInfo
from django.http import JsonResponse
# Create your views here.



class PetView(View):
    #宠物仓接口
    def get(self,request):
        #权限管理
        #print(request.session['user_id'])
        if 'user_id' not in request.session:
            # 用户未登录，返回未授权的错误信息
            return JsonResponse({'code': 401, 'message': "未授权"}, status=401)
        '''获取宠物列表'''
        user_id = request.session['user_id']
        petsInfo = PetsInfo.objects.all()
        petcabin = []
        for p in petsInfo:
            dict = {"id":p.pet_id,"name":p.pet_name,"level":p.level}
            petcabin.append(dict)
        return JsonResponse({'code': 1000, 'message': "获取成功","petcabin":petcabin})

    def post(self,request):
        '''添加及其他操作'''
    def delete(self,request):
        '''删除宠物'''