
from django.conf.urls import url
from django.contrib import admin
from Main import views as main
from LoginSystem import views as login
from DashBoard import views as dashboard
from FriendSystem import views as friend
from Multimedia import views as media

urlpatterns = {
    url(r'^admin/', admin.site.urls),

    # main app
    url(r'^article/', main.article),
    url(r'^$', main.index),
    url(r'^intro/', main.intro),
    url(r'^search/', main.search),
    url(r'^game/', main.game),

    # login app
    url(r'^register/', login.register),
    url(r'^adduser', login.adduser),
    url(r'^login/', login.login),
    url(r'^user_login/', login.user_login),
    url(r'^logout/', login.logout),

    # dashboard app
    url(r'^inbox/', dashboard.inbox),
    url(r'^dashboard/', dashboard.dashboard),
    url(r'^setting/', dashboard.setting),
    url(r'^wastebasket/', dashboard.wastebasket),
    url(r'^social/', dashboard.social),
    url(r'^postcontent/', dashboard.postcontent),
    url(r'^postblog/', dashboard.postblog),
    url(r'^chatview/(\S+)_to_(\S+)/$', dashboard.chatview),
    url(r'^blog/', dashboard.sblog),
    url(r'^updateuser/', dashboard.updateuser),
    url(r'^updatehead/', dashboard.updatehead),
    url(r'^userinfo/(\S+)/$', dashboard.userinfo),

    # friends app
    url(r'^getaddfriend/', friend.getaddfriend),
    url(r'^friends/', friend.friends),
    url(r'^agreeadd/(\S+)/$', friend.agreeadd),
    url(r'^disagreeadd/(\S+)/$', friend.disagreeadd),
    url(r'^known/(\S+)/$', friend.known),
    url(r'^sendmessage/(\S+)/$', friend.sendmessage),
    url(r'^send/(\S+)/$', friend.sendmessage_from_chatview),

    # mulyimedia
    url(r'^uploadvideo/', media.uploadvideo_view),
    url(r'^uploadvideoto/', media.uploadvideo),

}
