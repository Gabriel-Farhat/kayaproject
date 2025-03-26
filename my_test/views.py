# meu_aplicativo/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'home.html') 
def perfil(request, id):

    return render(request, 'components/perfil.html', {'id': id})  

def diandraperfil(request, id):
    return render(request, 'components/diandraperfil.html', {'id': id})

def brunoperfil(request, id):
    return render(request, 'components/brunoperfil.html', {'id': id})

def brunaperfil(request, id):
    return render(request, 'components/brunaperfil.html', {'id': id})

def andreiaperfil(request, id):
    return render(request, 'components/andreiaperfil.html', {'id': id})

def amandaperfil(request, id):
    return render(request, 'components/amandaperfil.html', {'id': id})

def alexandreperfil(request, id):
    return render(request, 'components/alexandreperfil.html', {'id': id})

def rafaelperfil(request, id):
    return render(request, 'components/rafaelperfil.html', {'id': id})

def mariaperfil(request, id):
    return render(request, 'components/mariaperfil.html', {'id': id})

def luisaperfil(request, id):
    return render(request, 'components/luisaperfil.html', {'id': id})

def jeanperfil(request, id):
    return render(request, 'components/jeanperfil.html', {'id': id})

def isabelaperfil(request, id):
    return render(request, 'components/isabelaperfil.html', {'id': id})

def hasllingperfil(request, id):
    return render(request, 'components/hasllingperfil.html', {'id': id})

def guilhermeperfil(request, id):
    return render(request, 'components/guilhermeperfil.html', {'id': id})

def carlosperfil(request, id):
    return render(request, 'components/carlosperfil.html', {'id': id})


def vitorperfil(request, id):
    return render(request, 'components/vitorperfil.html', {'id': id})

def vaniaperfil(request, id):
    return render(request, 'components/vaniaperfil.html', {'id': id})

def arailtonperfil(request, id):
    return render(request, 'components/arailtonperfil.html', {'id': id})