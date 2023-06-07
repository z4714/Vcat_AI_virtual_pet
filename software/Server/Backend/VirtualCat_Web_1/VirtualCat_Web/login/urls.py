#from .views import logout,logon,login
from django.urls import path
from .views import LoginView
urlpatterns = [
    #http://域名（ip:端口）/login/login
   '''
    path('login/',),
    path('logon/',logon,name='logon'),
    path('logout/', logout, name='logout'),
    '''
]
