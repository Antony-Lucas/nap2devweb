from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from helpdesk import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('helpdesk/', include('helpdesk.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]