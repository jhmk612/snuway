from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

urlpatterns=[
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', logout, {'next_page':'home'}, name='logout')


]