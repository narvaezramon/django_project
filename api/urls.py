from django.conf.urls import patterns, url
from . import views
from django.contrib import admin
urlpatterns = patterns(
    'api.views',
    url(r'^usuarios/$', 'usuario_list', name='usuario_list'),
    url(r'^usuarios/(?P<name>\S+)/(?P<password>\S+)$', 'usuario_detail', name='usuario_detail'),

    #url(r'^prueba/$', views.usuario_list),
)
