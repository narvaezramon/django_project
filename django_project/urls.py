from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    url(r'^', include('api.urls', namespace='api')),

]
