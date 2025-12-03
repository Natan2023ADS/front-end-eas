# Projeto Escola - Entrega para EA (Django)

Estrutura mínima do projeto para a disciplina. Contém:
- Modelos: Aluno, Curso, Produto
- Admin para Aluno/Curso/Produto
- Views: listagem de alunos e cursos
- Formulário para cadastrar Produto via site
- API DRF para listar alunos
- Configuração simples de JWT via Simple JWT (notas abaixo)

## Como usar (passos)
1. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate   # Linux / macOS
   venv\Scripts\activate    # Windows
   ```

2. Instale dependências:
   ```
   pip install -r requirements.txt
   ```

3. Aplique migrações:
   ```
   python manage.py migrate
   ```

4. Crie superuser para acessar admin:
   ```
   python manage.py createsuperuser
   ```

5. Rode o servidor:
   ```
   python manage.py runserver
   ```

6. Acesse:
   - Admin: http://127.0.0.1:8000/admin/
   - Alunos: http://127.0.0.1:8000/alunos/
   - Cursos: http://127.0.0.1:8000/cursos/
   - Cadastrar produto: http://127.0.0.1:8000/produto/new/
   - API listar alunos (GET): http://127.0.0.1:8000/api/alunos/

## JWT / Autenticação (opcional)
Este projeto já inclui `rest_framework` nas configurações. Para usar JWT:
1. Instale: `pip install djangorestframework-simplejwt`
2. No arquivo `escola/urls.py` adicione:
   ```py
   from rest_framework_simplejwt.views import (
       TokenObtainPairView,
       TokenRefreshView,
   )
   urlpatterns += [
       path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
       path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   ]
   ```
3. Faça requisições POST para `/api/token/` com `username` e `password` para obter `access` e `refresh`.

## Observações
- Este projeto é um ponto de partida. Dependendo da sua rubrica, podemos:
  - Adicionar paginação, filtros, autenticação,
  - Adicionar testes automatizados,
  - Documentação Swagger/OpenAPI,
  - Deploy no Heroku / Railway / Render.

