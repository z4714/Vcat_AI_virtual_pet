from .views import logout,logon,login,MyTokenObtainPairView
from django.urls import path

urlpatterns = [
    path("api/token", MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('login/',login,name='login'),
    path('logon/',logon,name='logon'),
    path('logout/', logout, name='logout'),
]
