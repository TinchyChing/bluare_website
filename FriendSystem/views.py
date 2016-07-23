'''
好友系统管理
'''
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from FriendSystem.models import Friends,AddMessage,MessageBox
from LoginSystem.models import Users
from django.contrib import messages
import json

online_users = Users.objects.exclude(is_online=False).count()

# 发送添加好友信息
def getaddfriend(request):
    email = request.POST.get('p_email')
    user = request.session.get('users')
    if email == user:
        messages.error(request,"您不能添加自己为好友")
    else:
        if not user:
            return HttpResponseRedirect('/login')
        AddMessage.objects.get_or_create(email=email)
        Friends.objects.get_or_create(email=user)
        addmsg = AddMessage.objects.get(email=email)
        msg_list = json.loads(addmsg.messsage)
        if email in msg_list:
            messages.error(request,"您已经发送过这条信息")
        elif not email in msg_list:
            msg_list.append(user)
            msg_list = json.dumps(msg_list)
            addmsg.messagege = msg_list
            addmsg.save()
            messages.info(request,"发送成功")
    return HttpResponseRedirect('/social')

# 好友管理页面
def friends(request):
    title = "好友"
    user = request.session.get('users')
    userinfo = Users.objects.get(email=user)
    AddMessage.objects.get_or_create(email=user)
    count_msg = AddMessage.objects.get(email=user)
    count_addmsg = json.loads(count_msg.message)
    count_addmsg = len(count_addmsg)
    try:
        Friends.objects.get(email=user)
    except Friends.DoesNotExist:
        Friends.objects.create(email=user)
    list_friends = Friends.objects.get(email=user)
    list_f = json.loads(list_friends.friends)
    return render(request, 'users/Dashboard/friends.html',{'online_users':online_users,'list_f':list_f,'userinfo':userinfo,'user':user, 'title':title,'count_addmsg':count_addmsg})

# 同意添加好友
def agreeadd(request,email):
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    else:
        try:
            if Friends.objects.get(email=user):
                new_friend = Friends.objects.get(email=user)
                friend_list = json.loads(new_friend.friends)
                add = Friends.objects.get(email=email)
                addlist = json.loads(add.friends)
                if not email in friend_list:
                    friend_list.append(email)
                    new_friend.friends = json.dumps(friend_list)
                    new_friend.save()
                    addlist.append(user)
                    add.friends = json.dumps(addlist)
                    add.save()
                    msg = AddMessage.objects.get(email=user)
                    msg_info = json.loads(msg.message)
                    msg_info.remove(email)
                    msg_info = json.dumps(msg_info)
                    msg.message = msg_info
                    msg.save()
                    messages.info(request,"添加成功")
                    return HttpResponseRedirect('/inbox')
                else:
                    messages.error(request,"您已经添加过此好友")
                    return HttpResponseRedirect('/inbox')
        except Friends.DoesNotExist:
            list = []
            Friends.objects.create(email=user)
            new_friend = Friends.objects.get(email=user)
            new_friend.friends = json.dumps(list)
            new_friend.save()
            new_friend = Friends.objects.get(email=user)
            friend_list = json.loads(new_friend.friends)
            add = Friends.objects.get(email=email)
            addlist = json.loads(add.friends)
            if not email in friend_list:
                friend_list.append(email)
                new_friend.friends = json.dumps(friend_list)
                new_friend.save()
                addlist.append(user)
                add.friends = json.dumps(addlist)
                add.save()
                msg = AddMessage.objects.get(email=user)
                msg_info = json.loads(msg.message)
                msg_info.remove(email)
                msg_info = json.dumps(msg_info)
                msg.message = msg_info
                msg.save()
                messages.info(request,"添加成功")
                return HttpResponseRedirect('/inbox')
            else:
                messages.error(request,"您已经添加过此好友")
                return HttpResponseRedirect('/inbox')

# 不同意添加好友
def disagreeadd(request,email):
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    else:
        AddMessage.objects.get_or_create(email=user)
        disagree = AddMessage.objects.get(email=user)
        disagreemsg = json.loads(disagree.message)
        disagreemsg.remove(email)
        AddMessage.objects.get_or_create(email=email)
        send = AddMessage.objects.get(email=email)
        sendmsg = json.loads(send.disagree)
        sendmsg.append(user)
        sendmsg = json.dumps(sendmsg)
        send.disagree = sendmsg
        send.save()
        disagree.message = json.dumps(disagreemsg)
        disagree.message = disagreemsg
        disagree.save()
        messages.info(request,"已拒绝添加请求")
        return HttpResponseRedirect('/inbox')

# 已读拒绝添加好友的消息，并删除此消息
def known(request,email):
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    AddMessage.objects.get_or_create(email=user)
    rmmsg =  AddMessage.objects.get(email=user)
    msg = json.loads(rmmsg.disagree)
    msg.remove(email)
    msg = json.dumps(msg)
    rmmsg.disagree = msg
    rmmsg.save()
    return HttpResponseRedirect('/inbox')

# 向好友发送信息
def sendmessage(request,email):
    content = request.POST.get('content')
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    send = MessageBox.objects.create(email=user)
    send.email_to = email
    send.content = content
    send.save()
    messages.info(request,"发送成功")
    return HttpResponseRedirect('/friends')

# 在聊天页面向好友发送消息
def sendmessage_from_chatview(request,email):
    content = request.POST.get('content')
    user = request.session.get('users')
    if not user:
        return HttpResponseRedirect('/login')
    send = MessageBox.objects.create(email=user)
    send.email_to = email
    send.content = content
    send.save()
    messages.info(request,"发送成功")
    return HttpResponseRedirect('/chatview/'+user+'_to_'+email)