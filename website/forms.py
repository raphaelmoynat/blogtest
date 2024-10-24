from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': 'Titre',         # Changed to French
            'content': 'Contenu',     # Changed to French
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le titre de l\'article'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Entrez le contenu de l\'article'}),
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = "__all__"
        labels = {
            'content': 'Votre commentaire',
        }
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Entrez votre commentaire'}),
        }

