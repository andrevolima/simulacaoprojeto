from django.urls import path
from . import views

urlpatterns = [
    path(r'^$',views.signIn),
    path(r'postindex/',views.signIn),
    path('campeonatos/', views.CampeonatoListCreate.as_view(), name='campeonato-list-create'),
    path('campeonatos/<int:pk>/', views.CampeonatoDetail.as_view(), name='campeonato-detail'),
    path('adicionar-campeonato/', views.adicionar_campeonato, name='adicionar-campeonato'),
    path('times/', views.TimeListCreate.as_view(), name='time-list-create'),
    path('times/adicionar/', views.adicionar_time, name='adicionar_time'),  # Nova rota para adicionar time
    path('times/<int:pk>/', views.TimeDetail.as_view(), name='time-detail'),
    path('jogadores/', views.JogadorListCreate.as_view(), name='jogador-list-create'),
    path('jogadores/<int:pk>/', views.JogadorDetail.as_view(), name='jogador-detail'),
    path('jogadores/<int:time_id>/adicionar/', views.adicionar_jogador, name='adicionar_jogador'),  # Nova rota para adicionar jogador
    path('tecnicos/<int:pk>/', views.TecnicoDetail.as_view(), name='tecnico-detail'),
]
