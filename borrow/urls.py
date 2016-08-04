
from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.lend_list, name='lendlist'),
    url(r'^(?P<pk>\d+)/$', views.lend_view, name='lend_view'),
    url(r'^(?P<pk>\d+)/comment/(?P<id>\d+)/$', views.edit_comment, name='edit_comment')

]
