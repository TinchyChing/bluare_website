'''
多媒体流处理系统，图像视频加载，图像视频传输系统
'''
import imghdr
from django.contrib import messages
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from FriendSystem.models import Friends,AddMessage,MessageBox
from LoginSystem.models import Users
from Multimedia.models import UsersVideo
import time
import os,json

online_users = Users.objects.exclude(is_online=False).count()

# 视频上传表
class VideoForm(forms.Form):
    title = forms.CharField()
    video = forms.FileField()
    type = forms.CharField()

# 视频上传函数
def uploadvideo(request):
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    video = VideoForm(request.POST,request.FILES)
    if video.is_valid():
        title = video.cleaned_data['title']
        video_file = video.cleaned_data['video']
        type = video.cleaned_data['type']
        try:
            UsersVideo.objects.get(email=user)
        except UsersVideo.DoesNotExist:
            UsersVideo.objects.create(email=user)
        user_video = UsersVideo.objects.get(email=user)
        user_video.title = title
        user_video.videos = video_file
        user_video.type = type
        user_video.save()
        messages.info(request,'上传成功')
    return HttpResponseRedirect('/uploadvideo')

def uploadvideo_view(request):
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    title = "上传视频"
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    return render(request, 'users/Dashboard/uploadvideo/uploadvideo.html',{'online_users':online_users,'userinfo':userinfo,'user':user,'title':title,'count_addmsg':count_addmsg})

    
