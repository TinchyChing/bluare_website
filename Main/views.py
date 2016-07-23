from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import render
from LoginSystem.models import Users
from DashBoard.models import PostContent

class SearchForm(forms.Form):
    search = forms.CharField()

online_users = Users.objects.exclude(is_online=False).count()

def index (request):
    title = "首页"
    user = request.session.get('users')
    images = [1,2,3,4,5,6,7]
    return render(request, 'index.html',{'online_users':online_users,'user':user, 'title':title,'images':images})

def search (request):
    title = "搜索"
    user = request.session.get('users')
    return render(request, 'users/search/search.html',{'online_users':online_users,'user':user, 'title':title})


def article(request):
    title = "文章"
    user = request.session.get('users')
    return render(request, 'users/article/article.html',{'online_users':online_users,'user':user})

def intro(request):
    title = "团队介绍"
    user = request.session.get('users')
    return render(request, 'teams/introduction.html',{'online_users':online_users,'title':title,'user':user})



def search_people(request):

    search_email = request.POST.get('search_info')
    search_email = "^" + str(search_email)

    search_result = Users.objects.filter(email__icontains=search_email)

    if search_result:
        message = "这是 " + search_email + " 的搜索结果"
        return HttpResponseRedirect('/search',{'message':message})


def game(request):
    title = "游戏"
    user = request.session.get('users')
    return render(request, 'products/games/index.html',{'user':user, 'title':title})

