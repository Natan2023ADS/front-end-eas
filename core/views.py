from django.shortcuts import render, redirect
from .models import Aluno, Curso
from .forms import ProdutoForm
from django.urls import reverse
from .forms import ProdutoForm, AlunoForm  # ✅ importe AlunoForm

def home(request):
    return render(request, 'home.html')

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

def aluno_new(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alunos_list')  # depois de salvar volta para listagem
    else:
        form = AlunoForm()

    return render(request, 'aluno_form.html', {'form': form})
