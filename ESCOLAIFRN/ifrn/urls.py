from django.urls import path
from . import views

urlpatterns = [
    path('rota1/', views.index, name = 'usuario'),
    path('rota2/', views.disciplinas, name = 'disciplina'),
    path('rota3/', views.autorizacao, name = 'autorizacao'),
    path('rota4/', views.livraria, name = 'livraria'),
    path('rota5/', views.melhordisciplinas, name = 'melhordisciplina'),
    path('rota6/', views.nivel, name = 'nivelPrioridade'),
    path('rota7/', views.lista, name = 'listalunos'),
    path('rota8/', views.ordemlista, name = 'ordemalunos'),
    path('alunos/', views.idlista, name='alunos'),
    path('rota9/<int:id>/', views.detalhes, name='detalhes'),
    path('rota9/<int:id>/', views.detalhes, name='detalhes'),
    path('rota10/', views.alerta, name='alerta'),
    
]