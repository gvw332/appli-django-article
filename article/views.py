from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ArticleForm
from .models import Article
from .models import Auteur
from .forms import AuteurForm

def accueil(request):
    return render( request, 'accueil.html')
def contact(request):
    return render(request, 'contact.html')


def liste_article(request):
    articles = Article.objects.all()  # Récupère tous les articles depuis la base de données
    return render(request, 'liste.html', {'articles': articles})
@login_required
def detail_article(request, id):
    # Utilisation de get_object_or_404 pour récupérer l'article correspondant à l'ID ou renvoyer une 404 si non trouvé
    article = get_object_or_404(Article, pk=id)

    return render(request, 'detail.html', {'article': article})

def creer_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre l'article dans la base de données
            return redirect('liste')  # Redirige après l'ajout de l'article
    else:
        form = ArticleForm()

    return render(request, 'creer_article.html', {'form': form})

@permission_required('article.Peut_Modifier_Article', raise_exception=True)
def update_article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('detail', id=article.id)
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'update_article.html', {'form': form, 'article': article})

def liste_auteurs(request):
    auteurs = Auteur.objects.all()
    return render(request, 'liste_auteurs.html', {'auteurs': auteurs})

def creer_auteur(request):
    if request.method == "POST":
        form = AuteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_auteurs')  # Redirigez vers une liste d'auteurs ou une autre page
    else:
        form = AuteurForm()
    return render(request, 'creer_auteur.html', {'form': form})

def supprimer_auteur(request, pk):
    auteur = get_object_or_404(Auteur, pk=pk)
    if request.method == "POST":
        auteur.delete()
        return redirect('liste_auteurs')
    return render(request, 'supprimer_auteur.html', {'auteur': auteur})

def supprimer_article( request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article.delete()
        return redirect('liste')
    return render(request, 'supprimer_article.html', {'article': article})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'article_detail.html', {'article': article})