# meu_aplicativo/urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),  # Rota para a página inicial
    path('perfil/<int:id>/', views.perfil, name='perfil'),  
    path('diandraperfil/<int:id>/', views.diandraperfil, name='diandraperfil'),
    path('brunoperfil/<int:id>/', views.brunoperfil, name='brunoperfil'),
    path('brunaperfil/<int:id>/', views.brunaperfil, name='brunaperfil'),
    path('andreiaperfil/<int:id>/', views.andreiaperfil, name='andreiaperfil'),
    path('amandaperfil/<int:id>/', views.amandaperfil, name='amandaperfil'),
    path('alexandreperfil/<int:id>/', views.alexandreperfil, name='alexandreperfil'),
    path('rafaelperfil/<int:id>/', views.rafaelperfil, name='rafaelperfil'),
    path('vitorperfil/<int:id>/', views.vitorperfil, name='vitorperfil'),
    path('vaniaperfil/<int:id>/', views.vaniaperfil, name='vaniaperfil'),
    path('mariaperfil/<int:id>/', views.mariaperfil, name='mariaperfil'),
    path('luisaperfil/<int:id>/', views.luisaperfil, name='luisaperfil'),
    path('jeanperfil/<int:id>/', views.jeanperfil, name='jeanperfil'),
    path('isabelaperfil/<int:id>/', views.isabelaperfil, name='isabelaperfil'),
    path('hasllingperfil/<int:id>/', views.hasllingperfil, name='hasllingperfil'),
    path('guilhermeperfil/<int:id>/', views.guilhermeperfil, name='guilhermeperfil'),
    path('carlosperfil/<int:id>/', views.carlosperfil, name='carlosperfil'),
    path('arailtonperfil/<int:id>/', views.arailtonperfil, name='arailtonperfil'),
]