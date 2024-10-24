from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from website.forms import ArticleForm, CommentForm
from website.models import Article


# Create your views here.
def index_articles(request):
    articles = Article.objects.all()
    return render(request, 'website/article_index.html', {'articles': articles})


def article_form_view(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'website/form.html', {"form": form})

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('show_article', article_id=article.id)

    return render(request, 'website/article_show.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form
    })

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('home')

def update_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('show_article', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'website/form.html', {'form': form, 'article': article})




