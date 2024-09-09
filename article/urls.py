from django.urls import path
from . import views
from .views import article_detail
urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('contact/', views.contact, name='contact'),

    path('liste/', views.liste_article, name='liste'), # liste-article
    path('article/<int:id>/', article_detail, name='article_detail'),
    path('<int:id>/', views.detail_article, name="detail"),    
    path('creer-article/', views.creer_article, name='creer_article'),
    path('modifier-article/<int:id>/', views.update_article, name='modifier_article'),
    path('supprimer/<int:pk>)/', views.supprimer_article, name='supprimer_article'),
    
    path('auteurs/', views.liste_auteurs, name='liste_auteurs'),
    path('creer-auteur/', views.creer_auteur, name='creer_auteur'),    
    path('supprimer-auteur/<int:pk>/', views.supprimer_auteur, name='supprimer_auteur'),
]
