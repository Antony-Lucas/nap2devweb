from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('edit_perfil', views.edit_perfil, name ='edit_perfil'),
    path('encomenda',views.encomenda,name='encomenda'),
    path('transport',views.transport,name='transport'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]