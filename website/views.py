from django.http import HttpResponse
from django.shortcuts import render, redirect

from website.forms import ArticleForm
from website.models import Article


# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'website/index.html', {'articles': articles})


def article_form_view(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'website/form.html', {"form": form})

