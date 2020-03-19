""" 定义users的URL模式 """

from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = 'users'

urlpatterns = [
    # 登录页面
    path('login/', LoginView.as_view(template_name='users/login.html'),
        name='login'),

    # 注册页面
    url(r'^register/$', views.register, name='register'),

    # 注销
    path('logout/', LogoutView.as_view(), name='logout'),
]