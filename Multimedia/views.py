'''
多媒体流处理系统，图像视频加载，图像视频传输系统
'''
import imghdr
from django.contrib import messages
from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from DashBoard.models import PostContent,Comment,T_Comment
from FriendSystem.models import Friends,AddMessage,MessageBox
from LoginSystem.models import Users
from Multimedia.models import UsersVideo
import time
import os,json


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
    video = VideoForm(request.POST,request,FILES)
    if video.is_vaild():
        title = head.cleaned_data['title']
        video_file = head.cleaned_data['video']
        type = head.cleaned_data['type']
        try:
            UsersVideo.objects.get(email=user)
        except UsersVideo.DoesNotExist:
            UsersVideo.objects.create(email=user)
        user_video = UsersVideo.objects.get(email=user)
        user_video.title = title
        user_video.videos = video_file
        user_video.type = type
        user_video.save()

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
    return render(request, 'users/Dashboard/uploadvideo/uploadvideo.html',{'userinfo':userinfo,'user':user,'title':title,'count_addmsg':count_addmsg})

    
