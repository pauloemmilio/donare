from django.conf.urls import url
from ong import views
urlpatterns = [

 url(r'^$', views.ongs_list, name='ongs_list'),
 url(r'^new$', views.ResistrarOng.as_view(), name='criar_ong'),
 url(r'^edit/(?P<pk>\d+)$', views.alterar_ong, name='alterar_ong'),
 url(r'^delete/(?P<pk>\d+)$', views.deletar_ong, name='deletar_ong'),
]
