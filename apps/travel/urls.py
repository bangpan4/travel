from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^travels$', views.dashboard),
    url(r'^travels/add$', views.addtrip),
    url(r'^travels/clear$', views.clear),
    url(r'^createtrip$', views.createtrip),
    url(r'^clear$', views.clear),
]