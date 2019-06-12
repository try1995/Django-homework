from django.shortcuts import render, HttpResponse
from django.views import View
from app01 import models
from django.db.models import Count, Sum, F
# Create your views here.

user_list = ['alex', 'try', 'dragon']


def test(request):
    # models.UserGroup.objects.create(title='vip1')
    # models.UserGroup.objects.create(title='vip2')
    # models.UserGroup.objects.create(title='vip3')
    # models.UserGroup.objects.create(title='vip4')
    # models.UserInfo.objects.create(user='卫', pwd='2123', ug_id=6)
    # models.UserInfo.objects.create(user='卫2', pwd='2123', ug_id=6)
    # models.UserInfo.objects.create(user='卫3', pwd='2123', ug_id=6)
    # obj = models.UserInfo.objects.all().first()
    # print(obj.user, obj.pwd, obj.ug_id, obj.ug.title)
    obj = models.UserInfo.objects.all().update(pwd='try')
    # print(obj.query)
    print(obj)
    # for i in obj.userinfo_set.all():
    #     print(i.user, i.pwd)
    return HttpResponse('...')


def index(request):
    return render(request, 'index.html', {'user_list': user_list})


def edit(request, a):
    print(a)
    return HttpResponse('...')


class Login(View):
    def dispatch(self, request, *args, **kwargs):
        print('begin')
        obj = super(Login, self).dispatch(request, *args, **kwargs)
        print('after')
        return obj

    def get(self, request):
        return render(request, 'login_test.html')

    def post(self, request):
        return HttpResponse('POST')
