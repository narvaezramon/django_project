from django.conf.urls import patterns, url
from . import views
from django.contrib import admin
urlpatterns = [

    #url(r'^usuario/$', views.usuario_list, name='usuario_list'),
    #url(r'^usuarios/(?P<user>)/(?P<pass>)+)$', 'usuario_detail', name='usuario_list'),

    url(r'^prueba/$', views.usuario_list),
]
