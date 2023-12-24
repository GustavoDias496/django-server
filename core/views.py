from django.shortcuts import render
from rest_framework import viewsets
from core.models import Category, Finalist, Episodes, Services, Post
from .serializers import CategorySerializer, FinalistSerializer, EpisodesSerializer, ServicesSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import permission_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.db import transaction
import json

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FinalistViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = Finalist.objects.all()
    serializer_class = FinalistSerializer


class EpisodesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = Episodes.objects.all()
    serializer_class = EpisodesSerializer


class ServicesViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )

    queryset = Post.objects.all()
    serializer_class = PostSerializer

@csrf_exempt
def vote(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        ids_categorias = data.get('idsCategorias', [])
        ids_finalistas = data.get('idsFinalistas', [])
        print("Ids Categorias:", ids_categorias)
        print("Ids Finalistas:", ids_finalistas)

        if len(ids_categorias) != len(ids_finalistas):
            return JsonResponse({'erro': 'Entrada inválida. As listas de categoria e finalista devem ter o mesmo comprimento.'}, status=400)

        try:
            for id_categoria, id_finalista in zip(ids_categorias, ids_finalistas):
                categoria = Category.objects.get(id=id_categoria)
                finalista = Finalist.objects.get(id=id_finalista, category=categoria)

                finalista.votes += 1
                finalista.save()

            return JsonResponse({'mensagem': 'Votos registrados com sucesso.'})

        except (Category.DoesNotExist, Finalist.DoesNotExist) as e:
            print(f"Erro: {e}")
            return JsonResponse({'erro': 'Um ou mais dados fornecidos não existem no banco de dados.'}, status=400)

    return JsonResponse({'erro': 'Método de solicitação inválido.'}, status=400)