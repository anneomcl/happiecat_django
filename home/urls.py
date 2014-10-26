from django.conf.urls import patterns, url

from home import views

urlpatterns = patterns('',
                       # ex: /home/
                       url(r'^$', views.index, name='index'),
                       url(r'^index.html$', views.index, name='index'),
                       url(r'^post.html$', views.post, name='post'),
                       url(r'^project0.html$', views.project0, name='project0'),
                       url(r'^about.html$', views.about, name='about'),
                       url(r'^contact.html$', views.contact, name='contact'),
                       #url(r'^post/(?P<project_ID>\d+)/$', views.project, name='project')
                       # ex: /home/5/
                       #url(r'^(?P<question_id>\d+)/$', views.detail, name='detail')
)