from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from transportadora import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transportadora.urls')),
]