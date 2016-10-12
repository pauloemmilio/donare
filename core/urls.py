from django.conf.urls import url
from core import views
urlpatterns = [
 url(r'^$', views.index, name='index'),
 url(r'^ong/$', views.ong, name='ong'),
]
