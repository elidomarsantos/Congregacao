
import django
from django import urls
from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('designacoes.urls')),
    path('contatos/', include('contatos.urls')),
    path('autenticacao/', include('django.contrib.auth.urls')),
    path('contas/', include('contas.urls')),

]
