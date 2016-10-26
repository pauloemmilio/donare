from django.conf.urls import url
from doador import views
urlpatterns = [
	url(r'^cadastrar', views.cadastrar_doador, name='cadastrar'),
	url(r'^(?P<doador_id>[0-9]+)/editar', views.editar_doador, name='editar_doador'),
	url(r'^(?P<doador_id>[0-9]+)/', views.profile, name='profile'),
	url(r'^deletar/(?P<doador_id>[0-9]+)/', views.deletar_doador, name='deletar_doador'),
]
