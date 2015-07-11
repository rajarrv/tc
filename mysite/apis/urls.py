from django.conf.urls import patterns, url

from apis import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    #url(r'^/index1/$', views.index1, name='index1'),
    url(r'^search$', views.search, name='search'),
    url(r'^login/$', views.login, name='login'),
    url(r'^insert/$', views.insert, name='insert'),
    url(r'^show_files/$', views.show_files, name='show_files'),
    url(r'^mongostatus/$', views.mongostatus, name='mongostatus'),
)