from django.conf.urls import patterns, url

from goodLuck import views

urlpatterns = patterns('',
  url(r'^$', views.goodLuck_list, name='goodLuck_list'),
  url(r'^new$', views.goodLuck_create, name='goodLuck_new'),
  url(r'^edit/(?P<pk>\d+)$', views.goodLuck_update, name='goodLuck_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.goodLuck_delete, name='goodLuck_delete'),  
  url(r'^export/csv/$', views.export_users_csv, name='export_users_csv'),
)