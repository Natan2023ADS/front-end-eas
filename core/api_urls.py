from django.urls import path
from .api_views import AlunoListAPI

urlpatterns = [
    path('alunos/', AlunoListAPI.as_view(), name='api_alunos_list'),
]
