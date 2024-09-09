from django import forms
from .models import Article, Auteur


class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'
    def clean_nom(self):

        nom = self.cleaned_data['nom']
        if 'batman' in nom.lower():
            raise forms.ValidationError("Le nom doit être correct !")
        return nom   
    
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'date_publication', 'auteur', 'image']  

        widgets = {
            'date_publication': forms.DateInput(format="%d-%m-%Y", attrs={"type": "date"})
        }

