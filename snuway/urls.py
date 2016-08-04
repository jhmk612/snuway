
from django.conf.urls import url, include
from django.contrib import admin
from index import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^lend/', include('lend.urls', namespace='lend')),
    url(r'^borrow/', include('borrow.urls', namespace='borrow'))
]
