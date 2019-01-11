from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from dashboard import views

urlpatterns = [
    url(r'^$', views.user_login, name='index'),
    url(r'^signup/$', views.register, name='signup'),
    url(r'^signin/$', views.user_login, name='signin'),
    url(r'^signout/$', views.logout_user, name='signout'),
    url(r'^index/$', login_required(views.HomePage.as_view()), name='homepage'),
    url(r'^add/task/$', login_required(views.AddTask.as_view()), name='addtask'),
    url(r'^task/(?P<taskid>.*?)/(?P<action>.*?)/$', login_required(views.ObjectHandler.as_view()), name='object handler'),
    url(r'^task/(?P<status>.*?)/$', login_required(views.TaskStatus.as_view()), name='task status'),
]