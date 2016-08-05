
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.lend_list, name='lendlist'),
    url(r'^post/(?P<pk>\d+)/$', views.lend_view, name='lend_view'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.lend_edit, name='lend_edit'),
    url(r'^post/(?P<pk>\d+)/comment/(?P<id>\d+)/$', views.edit_comment, name='edit_comment'),
    url(r'^post/(?P<pk>\d+)/comment/(?P<id>\d+)/delete/$', views.delete_comment, name='delete_comment'),

]
