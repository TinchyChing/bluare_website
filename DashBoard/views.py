import imghdr
from django.contrib import messages
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from DashBoard.models import PostContent,Comment,T_Comment
from FriendSystem.models import Friends,AddMessage,MessageBox
from LoginSystem.models import Users
import time
import os,json

class HeadForm(forms.Form):
    head = forms.ImageField()

# 通用显示好友信息,请求信息数量

# Create your views here.

def dashboard(request):
    title = "仪表盘"
    user = request.session.get('users')
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    if not user:
        return HttpResponseRedirect('/login')
    return render(request, 'users/Dashboard/dashboard.html',{'userinfo':userinfo,'user':user,'title':title,'count_addmsg':count_addmsg})

def inbox(request):
    title = "消息"
    user = request.session.get('users')
    users = Users.objects.all()
    userinfo = Users.objects.get(email=user)    # 用户信息
    AddMessage.objects.get_or_create(email=user)    # 读取用户的添加好友信息
    count_msg = AddMessage.objects.get(email=user)  # 读取信息个数

    list_msg = json.loads(count_msg.message)    # 读取信息个数
    count_dismsg = AddMessage.objects.get(email=user)   # 读取信息个数
    dis_msg = json.loads(count_dismsg.disagree)   # 读取信息个数
    count_addmsg = len(list_msg)   # 读取信息个数
    count_dis_msg = len(dis_msg)   # 读取信息个数

    message = MessageBox.objects.order_by('-id').all()
    if not user:
        return HttpResponseRedirect('/login')
    return render(request, 'users/Dashboard/inbox.html',{'users':users,'message':message,'dis_msg':dis_msg,'list_msg':list_msg,'userinfo':userinfo,'user':user, 'title':title,'count_addmsg':count_addmsg,'count_dis_msg':count_dis_msg})

def wastebasket(request):
    title = "回收站"
    user = request.session.get('users')
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    if not user:
        return HttpResponseRedirect('/login')
    return render(request, 'users/Dashboard/wastebasket.html',{'userinfo':userinfo,'user':user, 'title':title,'count_addmsg':count_addmsg})

def setting(request):
    title = "个人设置"
    user = request.session.get('users')
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    if not user:
        return HttpResponseRedirect('/login')
    return render(request, 'users/Dashboard/setting.html',{'user':user, 'title':title,'userinfo':userinfo,'count_addmsg':count_addmsg})

def social(request):
    title = "社交"
    allusers = Users.objects.all()
    blogcount = PostContent.objects.exclude(title="").count()
    contentcount = PostContent.objects.count() - blogcount
    postcontent = PostContent.objects.order_by('-id').all()
    user = request.session.get('users')
    Friends.objects.get_or_create(email=user)
    friends = Friends.objects.get(email=user)
    list = json.loads(friends.friends)
    friends_list = len(list)
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    if not user:
        return HttpResponseRedirect('/login')
    return render(request, 'users/Dashboard/social.html',{'userinfo':userinfo,
                                                          'blogcount':blogcount,
                                                          'allusers':allusers,
                                                          'user':user,
                                                          'title':title,
                                                          'postcontent':postcontent,
                                                          'contentcount':contentcount,
                                                          'friends_list':friends_list,
                                                          'list':list,
                                                          'count_addmsg':count_addmsg})

def postcontent(request):
    content = request.POST.get('p_content')
    user = request.session.get('users')
    todaydate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if not user:
        return HttpResponseRedirect('/login')
    if request.session.get('users'):
        PostContent.objects.create(email=user,content=content,date=todaydate)
        return HttpResponseRedirect('/social')

def updateuser(request):
    username = request.POST.get('p_username')
    birthday = request.POST.get('p_birthday')
    phone = request.POST.get('p_phone')
    country = request.POST.get('p_country')
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    todaydate = time.strftime("%Y/%m/%d", time.localtime())
    todayyear = int(todaydate[0]+todaydate[1]+todaydate[2]+todaydate[3])
    todaymonth = int(todaydate[5]+todaydate[6])
    todayday = int(todaydate[8]+todaydate[9])
    borndate = birthday
    bornyear = int(borndate[0]+borndate[1]+borndate[2]+borndate[3])
    bornmonth = int(borndate[5]+borndate[6])
    bornday = int(borndate[8]+borndate[9])
    o_age = todayyear - bornyear
    o_day = todayday - bornday
    if todaymonth - bornmonth > 0:
        pass
    else:
        if o_day > 0:
            pass
        else:
            o_age = o_age - 1
    age = o_age
    update = Users.objects.get(email=user)
    update.email=user
    update.username=username
    update.birthday=birthday
    update.phone=phone
    update.country=country
    update.age=age
    update.save()
    return HttpResponseRedirect('/setting')


def postblog(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    todaydate = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    if user:
        PostContent.objects.create(email=user,title=title,content=content,date=todaydate)
    return HttpResponseRedirect('/social')


def sblog(request):
    title = "发表博文"
    user = request.session.get('users')
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    if not user:
        return HttpResponseRedirect('/login')
    return render(request, 'users/Dashboard/postcontent/blog.html',{'userinfo':userinfo,'user':user,'title':title,'count_addmsg':count_addmsg})


def updatehead(request):
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    user = request.session.get('users')
    head = HeadForm(request.POST,request.FILES)
    if head.is_valid():
        headimg = head.cleaned_data['head']
        image_type = imghdr.what(headimg)
        if image_type == "png":
            userinfo = Users.objects.get(email=user)
            userinfo.head = headimg
            userinfo.save()
            userinfo = Users.objects.get(email=user)
            head = str(userinfo.head)
            os.rename(head,'static/upload/head/%s.png'%user)
            userinfo.head = 'static/upload/head/%s.png'%user
            userinfo.save()
    return HttpResponseRedirect('/setting')


def userinfo(request,email):
    user = request.session.get('users')
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    try:
        if Users.objects.get(email=email):
            showinfo = Users.objects.get(email=email)
            return render(request, 'users/Dashboard/userinfo/userinfo.html',{'userinfo':userinfo,'user':user,'showinfo':showinfo,'count_addmsg':count_addmsg})
    except Users.DoesNotExist:
        messages.error(request,"此用户不存在")
        return render(request, 'users/Dashboard/userinfo/userinfo.html',{'userinfo':userinfo,'user':user,'count_addmsg':count_addmsg})

# 聊天页面
def chatview(request, email, email_to):
    user = request.session.get('users')
    userinfo = Users.objects.get(email=user)
    if not user:
        return HttpResponseRedirect('/login')
    message = MessageBox.objects.order_by('id').all()
    return render(request, 'users/Dashboard/postcontent/chatview.html',{'userinfo':userinfo,'user':user,'email':email,'email_to':email_to,'message':message})
