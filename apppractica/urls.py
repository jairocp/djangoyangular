from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index,  name='index'),
    url(r'^ajaxp$',views.ajaxp, name='ajaxp'),
    url(r'^create$',views.create,name='create'),
    url(r'^inicio$',views.inicio,name='inicio'),
]