from django.conf.urls import url
from doador import views
urlpatterns = [
	url(r'^cadastrar', views.cadastrar_doador, name='cadastrar'),
	url(r'^(?P<doador_id>[0-9]+)/editar', views.editar_doador, name='editar_doador'),
]
