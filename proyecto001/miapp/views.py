
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layout = """
    <h1> Proyecto Web (LP3) | Flor Cerdán </h1>
    <hr/>
    <ul>
    <li>
    <a href="/inicio"> Inicio</a>
    </li>
    <li>
    <a href="/saludo"> Mensaje de Saludo</a>
    </li>
    <li>
    <a href="/rango"> Mostrar Números [a,b]</a>
    </li>
    <li>
    <a href="/rango2/10/15"> Mostrar Números [10,15]</a>
    </li>
    </ul>
    <hr/>
"""

def index(request):
    estudiantes = [ 'Willy Delgado', 
                    'Jhon Wick',
                    'Peter Parker',
                    'Clark Kent']
    estudiantes = []
    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web Con DJango',
        'estudiantes': estudiantes
    })

def saludo(request):
    return render(request,'saludo.html'),{
        'titulo':'saludo',
        'autor_saludo':'Willy Delgado Tuanama'
    }

def rango(request):
    a = 10
    b = 20
    rango_numeros = range(a,b+1)
    return render(request,'rango.html',{
        'titulo':'Rango',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })

def rango2(request):
    a = 10
    b = 15
    rango_numeros = range(a,b+1)
    return render(request,'rango2.html',{
        'titulo':'Rango 2',
        'a':a,
        'b':b,
        'rango_numeros':rango_numeros
    })
