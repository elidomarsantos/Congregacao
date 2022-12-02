from django.urls import path

from . import views



urlpatterns = [
    path('add_contatos/', views.add_contatos),
    path('view_contatos/', views.view_contatos),
    path('editar_contato/<int:id>', views.editar_contato),
    path('deletar_contato/<int:id>', views.deletar_contato),
   
]