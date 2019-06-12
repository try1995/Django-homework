"""my_jango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.shortcuts import HttpResponse, render, redirect
from app01 import views


def login(request):
    # return HttpResponse("try")
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        if u == 'root' and p == '123':
            return redirect('http://www.baidu.com')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('app01/', include('app01.urls')),
    path('test.html', views.test),
    re_path('login.html$', views.Login.as_view())
]

