from django.shortcuts import render, redirect
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Campeonato, Time, Jogador, Tecnico
from .serializers import CampeonatoSerializer, TimeSerializer, JogadorSerializer, TecnicoSerializer
from django.http import JsonResponse
import pyrebase

class CampeonatoListCreate(generics.ListCreateAPIView):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer

class CampeonatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer

class TimeListCreate(generics.ListCreateAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class TimeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

class JogadorListCreate(generics.ListCreateAPIView):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

class JogadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

class TecnicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

config = {
   'apiKey': "AIzaSyBWy9OCAKP3NR4dFPLfSUzzk-QXLBkdZmY",
   'authDomain': "teste-saudekids.firebaseapp.com",
   'projectId': "teste-saudekids",
   'storageBucket': "teste-saudekids.appspot.com",
   'messagingSenderId': "103564023514",
   'appId': "1:103564023514:web:702908e4968a10ba1a77e3",
   'databaseURL': "postgresql://postgres:admin@localhost:5432/FabricaTeste"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

def signIn(request):
    return render(request, "index.html")

def postsign(request):
    return render(request, "times.html")



@api_view(['POST'])
def adicionar_campeonato(request):
    if request.method == 'POST':
        serializer = CampeonatoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def campeonatos_page(request):
    campeonatos = Campeonato.objects.all()
    serializer = CampeonatoSerializer(campeonatos, many=True)
    return render(request, 'index.html', {'campeonatos': serializer.data})
    
def times_page(request):
    campeonatos = Campeonato.objects.all()
    serializer = CampeonatoSerializer(campeonatos, many=True)
    return render(request, 'times.html', {'campeonatos': serializer.data})

def jogadores_page(request, time_id):
    time = Time.objects.get(pk=time_id)
    jogadores = Jogador.objects.filter(time=time)
    serializer = JogadorSerializer(jogadores, many=True)
    return render(request, 'jogadores.html', {'jogadores': serializer.data})

def adicionar_time(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        campeonato_id = request.POST.get('campeonato_id')
        campeonato = Campeonato.objects.get(pk=campeonato_id)
        time = Time.objects.create(campeonato=campeonato, nome=nome, senha=senha)
        return redirect('times_page')
    return JsonResponse({'error': 'Método inválido'}, status=400)

def adicionar_jogador(request, time_id):
    if request.method == 'POST':
        time = Time.objects.get(pk=time_id)
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        jogador = Jogador.objects.create(time=time, nome=nome, idade=idade)
        return redirect('jogadores_page', time_id=time_id)
    return JsonResponse({'error': 'Método inválido'}, status=400)