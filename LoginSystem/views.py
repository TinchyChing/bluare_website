import json

from django.http import HttpResponseRedirect
from django.shortcuts import render

from FriendSystem.models import Friends
from LoginSystem.models import Users
from django.contrib import messages

def register(request):
    title = "注册"
    user = request.session.get('users')
    if user:
        return HttpResponseRedirect('/')
    return render(request, 'users/register.html',{'user':user,'title':title})

def login(request):
    title = "登陆"
    user = request.session.get('users')
    return render(request, 'users/login.html',{'user':user,'title':title})

def adduser(request):
    email = request.POST.get('r_email')
    password = request.POST.get('r_password')
    repeat_password = request.POST.get('r_rpassword')

    email = str(email)
    password = str(password)
    repeat_password = str(repeat_password)

    if email == None:
        error = False
        messages.error(request,"请输入邮箱")
        return HttpResponseRedirect('/register')
    if password == None:
        messages.error(request,"密码输入错误")
        return HttpResponseRedirect('/register')
    if repeat_password == None:
        messages.error(request,"两次密码输入不相同")
        return HttpResponseRedirect('/register')
    if password == repeat_password:
        if Users.objects.filter(email=email):
            error = False
            messages.error(request,"此邮箱已存在")
            return HttpResponseRedirect('/register')
        if not Users.objects.filter(email=email):
            error = True
            new_user = Users(email=email)
            new_user.password = password
            new_user.username = email+"xt"
            new_user.birthday = "0000-00-00"
            new_user.phone = 888888888
            new_user.country = "Country"
            new_user.save()
            Friends.objects.get_or_create(email=email)
            add = Friends.objects.get(email=email)
            friends = json.loads(add.friends)
            friends.append(email)
            add.friends = json.dumps(friends)
            add.save()
            messages.info(request,"成功注册")
            return HttpResponseRedirect('/login')

    if not password == repeat_password:
        error = False
        message = "两次密码输入的不一致"
        return HttpResponseRedirect('/register')

def user_login(request):

    email = request.POST.get('l_email')
    password = request.POST.get('l_password')

    email = str(email)
    password = str(password)

    try:
        user = Users.objects.get(email= email)
        if user:
            if user.password == password:
                messages.info(request,"成功登陆")
                request.session['users'] = email
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"密码输入错误")
                return HttpResponseRedirect('/login')
    except Users.DoesNotExist:
        return HttpResponseRedirect('/login')




def logout(request):
    try:
        del request.session['users']
    except KeyError:
        pass
    return HttpResponseRedirect('/')
# Create your views here.