from django.conf.urls import url
from doador import views
urlpatterns = [
	url(r'^cadastrar', views.cadastrar_doador, name='cadastrar'),
]
