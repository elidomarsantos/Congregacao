from django.urls import path

from . import views



urlpatterns = [
    path('', views.home),
    path('mapa/', views.mapa),
    path('escritorio/', views.escritorio),
    path('fotos/', views.fotos),
    path('local/', views.local),
    path('limpeza/', views.limpeza),
    path('reunioes/', views.reunioes),
    path('congresso/', views.congresso),
    path('grupos/', views.grupos),
    path('relatorio/', views.relatorio),
    path('visita/', views.visita),
    path('restrita/', views.restrita),
    path('desig_quarta/', views.desig_quarta),
    path('desig_sabado/', views.desig_sabado),
    path('historico_quarta/', views.historico_quarta),
    path('historico_sabado/', views.historico_sabado),
    path('editar_quarta/<int:id>', views.editar_quarta),
    path('deletar_quarta/<int:id>', views.deletar_quarta),
    path('editar_sabado/<int:id>', views.editar_sabado),
    path('deletar_sabado/<int:id>', views.deletar_sabado),
    path('indicadores/', views.indicadores),
    path('indicador_quarta/<int:id>', views.indicador_quarta),
    path('indicador_sabado/<int:id>', views.indicador_sabado),
    path('desig_coordenador/', views.desig_coordenador),
    path('desig_coordenador_quarta/<int:id>', views.desig_coordenador_quarta),
    path('desig_conferencia/', views.desig_conferencia),
    path('desig_conferencia2/<int:id>', views.desig_conferencia2),
 
    
    


]    