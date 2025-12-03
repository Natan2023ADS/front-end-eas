from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),            # 
    path('alunos/', views.alunos_list, name='alunos_list'),
    path('aluno/new/', views.aluno_new, name='aluno_new'),   # ✅ novo
    path('cursos/', views.cursos_list, name='cursos_list'),
    path('produto/new/', views.produto_new, name='produto_new'),
]
