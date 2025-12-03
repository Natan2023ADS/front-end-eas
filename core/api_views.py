from rest_framework import generics
from .models import Aluno
from .serializers import AlunoSerializer
from rest_framework.permissions import AllowAny

class AlunoListAPI(generics.ListAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [AllowAny]
