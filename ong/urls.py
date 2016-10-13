from django.conf.urls import url
from ong import views
urlpatterns = [

 url(r'^$', views.index, name='index'),
 url(r'^new', views.criar_ong, name='criar'),
 url(r'^edit/(?P<pk>\d+)$', views.alterar_ong, name='alterar_ong'),
 url(r'^delete/(?P<pk>\d+)$', views.deletar_ong, name='deletar_ong'),
 url(r'^ong', views.ong, name='ong'),
]
