from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^home/', include('home.urls', namespace="home")),
                       url(r'^admin/', include(admin.site.urls)),
                       )