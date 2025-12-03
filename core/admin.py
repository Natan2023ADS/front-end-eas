from django.contrib import admin
from .models import Aluno, Curso, Produto

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome','sobrenome','email')
    search_fields = ('nome','sobrenome','email')

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome','preco','validade')
    search_fields = ('nome',)
