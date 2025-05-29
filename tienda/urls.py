from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='base'),
    path('', views.home, name='home'),
    path('juegos_mesa/', views.juegos_mesa, name='juegos_mesa'),  # Ruta temporal
    path('miniaturas/', views.miniaturas, name='miniaturas'),  # Ruta temporal
    path('pandemic/', views.pandemic, name='pandemic'),  # Ruta temporal
    path('cursos_reservas/', views.cursos_reservas, name='cursos_reservas'),
    path('modelado/', views.modelado, name='modelado'),
    path('foro/', views.foro, name='foro'),
    path('dixit/', views.dixit, name='dixit'),  # Ruta temporal
    path('carcason/', views.carcason, name='carcason'),  # Ruta temporal
    path('catan/', views.catan, name='catan'),
    path('azul/',    views.azul,    name='azul'),
    path('terra/',   views.terra,   name='terra'),
    path('code/',    views.code,    name='code'),
    path('7wond/',   views.siete_wonders, name='7wond'),
    path('guardia/', views.guardia, name='guardia'),
    path('orc/',     views.orc,     name='orc'),
    path('elfos/',   views.elfos,   name='elfos'),
    path('mages/',   views.mages,   name='mages'),
    path('goblin/',  views.goblin,  name='goblin'),
    path('giant/',   views.giant,   name='giant'),
    path('lobo/',    views.lobo,    name='lobo'),
    path('dragon/',  views.dragon,  name='dragon'),
    path('cursouno/',   views.cursouno,    name='cursouno'),
    path('eventouno/',  views.eventouno,  name='eventouno'),
    path('cursodos/',   views.cursodos,    name='cursodos'),
    path('eventodos/',  views.eventodos,  name='eventodos'),
    path('cursotres/',   views.cursotres,    name='cursotres'),
    path('eventotres/',  views.eventotres,  name='eventotres'),
    path('cursocuatro/',   views.cursocuatro,    name='cursocuatro'),
    path('eventocuatro/',  views.eventocuatro,  name='eventocuatro'),
]
