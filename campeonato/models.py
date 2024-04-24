from django.db import models

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Time(models.Model):
    campeonato = models.ForeignKey(Campeonato, related_name='times', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

class Jogador(models.Model):
    time = models.ForeignKey(Time, related_name='jogadores', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

class Tecnico(models.Model):
    time = models.OneToOneField(Time, related_name='tecnico', on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
