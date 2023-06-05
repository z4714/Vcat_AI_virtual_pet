from django.shortcuts import render #默认导入
from django.http import HttpResponse 

# Create your views here.定义视图函数
def index(request):
    return render(request,'1/index.html')