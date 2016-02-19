from django.conf.urls import patterns, url
from . import views
from django.contrib import admin
urlpatterns = [

    url(r'^usuarios/$', views.usuario_list, name='usuario_list'),
    url(r'^usuarios/(?P<name>\S+)/(?P<password>\S+)$', views.usuario_detail, name='usuario_detail'),

    #url(r'^prueba/$', views.usuario_list),
]
