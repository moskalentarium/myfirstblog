from django.conf.urls import url, include
from django.urls import path
from . import views



urlpatterns = [
    url(r'^aboutme/$', views.index, name='index'),
    url(r'^$', views.glav, name='glav'),
    url(r'^gallery/$', views.foto, name = 'foto'),
]
