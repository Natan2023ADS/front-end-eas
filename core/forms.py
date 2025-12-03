from django import forms
from .models import Produto, Aluno   # ✅ adicione Aluno aqui

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','descricao','preco','validade']


class AlunoForm(forms.ModelForm):   # ✅ novo formulário
    class Meta:
        model = Aluno
        fields = ['nome', 'sobrenome', 'email']
