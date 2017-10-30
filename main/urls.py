from django.conf.urls import url, include
from django.contrib import admin
from . import views


urlpatterns = [
    url(regex=r'^$', view=views.catch_data, name='index'),
]