#coding=utf8

from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.joke_index),
    url(r'^operating_joke_from_user/',views.operating_joke_from_user)

]
