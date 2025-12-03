from django.shortcuts import render, redirect
from .models import Aluno, Curso
from .forms import ProdutoForm
from django.urls import reverse

def alunos_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos_list.html', {'alunos': alunos})

def cursos_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos_list.html', {'cursos': cursos})

def produto_new(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('produto_new'))
    else:
        form = ProdutoForm()
    return render(request, 'produto_form.html', {'form': form})
