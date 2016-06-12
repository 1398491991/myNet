#coding=utf8

from django.conf.urls import url
import views
urlpatterns = [
    url(r'^register/$', views.user_register),
    url(r'^login/$', views.user_login),
    url(r'^index/$', views.user_index),
    url(r'^out_login/$', views.user_out_login),
    url(r'^get_user_data/$',views.get_user_data),
]
