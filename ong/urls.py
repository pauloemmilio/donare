from django.conf.urls import url
from ong import views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

 url(r'^$', views.index, name='index'),
 
 url(r'^new', views.criar_ong, name='criar'),
 url(r'^$', views.login_ong, name='logar'),
 url(r'^ong/(?P<ong_id>[0-9]+)/edit', views.alterar_ong, name='alterar_ong'),
 url(r'^ong/delete/(?P<ong_id>[0-9]+)/', views.deletar_ong, name='deletar_ong'),
 url(r'^ong/(?P<ong_id>[0-9]+)/', login_required(views.ong), name='ong'),
 url(r'^ong/despesas/(?P<ong_id>[0-9]+)/new', views.criar_despesas, name='criar_despesas'),
 url(r'^ong/despesas/(?P<ong_id>[0-9]+)/edit/(?P<despesas_id>[0-9]+)', views.alterar_despesas, name='alterar_despesas'),
 url(r'^ong/despesas/(?P<ong_id>[0-9]+)/delete(?P<despesas_id>[0-9]+)/', views.deletar_despesas, name='deletar_despesas'),
url(r'^logout/', login_required(views.logout_page), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
