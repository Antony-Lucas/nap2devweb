from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('edit_perfil', views.edit_perfil, name ='edit_perfil'),
    path('encomenda',views.encomenda,name='encomenda'),
    path('encomendas/cadastrar/', views.cadastrar_encomenda, name='cadastrar_encomenda'),
    path('encomendas/editar/<int:pk>/', views.editar_encomenda, name='editar_encomenda'),
    path('encomendas/excluir/<int:pk>/', views.excluir_encomenda, name='excluir_encomenda'),
    path('transport',views.transport,name='transport'),
    path('logout/', views.logout_view, name='logout'),
]