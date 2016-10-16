from django.conf.urls import url
from ong import views
urlpatterns = [

 url(r'^$', views.index, name='index'),
 url(r'^new', views.criar_ong, name='criar'),
 url(r'^ong/(?P<ong_id>[0-9]+)/edit', views.alterar_ong, name='alterar_ong'),
 url(r'^ong/delete/(?P<ong_id>[0-9]+)/', views.deletar_ong, name='deletar_ong'),
 url(r'^ong/(?P<ong_id>[0-9]+)/', views.ong, name='ong'),
]
