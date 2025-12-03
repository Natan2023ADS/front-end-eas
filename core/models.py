from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nome} {self.sobrenome}"

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    alunos = models.ManyToManyField(Aluno, related_name='cursos', blank=True)

    def __str__(self):
        return self.titulo

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
