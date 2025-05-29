from django.shortcuts import render

def base(request):
    return render(request, 'tienda/base.html')

def home(request):
    return render(request, 'tienda/home.html')

def juegos_mesa(request):
    return render(request, 'tienda/juegos_mesa.html')

def miniaturas(request):
    return render(request, 'tienda/miniaturas.html')

def pandemic(request):
    return render(request, 'tienda/pandemic.html')

def dixit(request):
    return render(request, 'tienda/dixit.html')

def carcason(request):
    return render(request, 'tienda/carcason.html')

def azul(request):
    return render(request, 'tienda/azul.html')

def terra(request):
    return render(request, 'tienda/terra.html')

def code(request):
    return render(request, 'tienda/code.html')

# Como Python no permite nombres empezando por dígito, usamos siete_wonders
def siete_wonders(request):
    return render(request, 'tienda/7wond.html')

def guardia(request):
    return render(request, 'tienda/guardia.html')

def orc(request):
    return render(request, 'tienda/orc.html')

def elfos(request):
    return render(request, 'tienda/elfos.html')

def mages(request):
    return render(request, 'tienda/mages.html')

def goblin(request):
    return render(request, 'tienda/goblin.html')

def giant(request):
    return render(request, 'tienda/giant.html')

def lobo(request):
    return render(request, 'tienda/lobo.html')

def dragon(request):
    return render(request, 'tienda/dragon.html')
def catan(request):
    return render(request, 'tienda/catan.html')

def cursos_reservas(request):
    return render(request, 'tienda/cursos_reservas.html')

def modelado(request):
    return render(request, 'tienda/modelado.html')

def foro(request):
    return render(request, 'tienda/foro.html')

def cursouno(request):
    return render(request, 'tienda/cursouno.html')

def eventouno(request):
    return render(request, 'tienda/eventouno.html')
def cursodos(request):
    return render(request, 'tienda/cursodos.html')

def eventodos(request):
    return render(request, 'tienda/eventodos.html')
def cursotres(request):
    return render(request, 'tienda/cursotres.html')

def eventotres(request):
    return render(request, 'tienda/eventotres.html')
def cursocuatro(request):
    return render(request, 'tienda/cursocuatro.html')

def eventocuatro(request):
    return render(request, 'tienda/eventocuatro.html')