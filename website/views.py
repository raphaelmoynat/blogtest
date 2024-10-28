from datetime import timezone, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from website.forms import ArticleForm, CommentForm, RegisterForm, LoginForm
from website.models import Article, Comment

from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index_articles(request):
    articles = Article.objects.all()
    return render(request, 'website/article_index.html', {'articles': articles})


def article_form_view(request):
    if request.user.is_authenticated:
        form = ArticleForm()
        if request.method == 'POST':
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save(commit=False)
                article.author = request.user
                article.save()
                return redirect('home')
        return render(request, 'website/form.html', {"form": form})
    else:
        return redirect('home')

def show_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()

    comment_form = None


    if request.user.is_authenticated:
        comment_form = CommentForm()
        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.article = article
                comment.author = request.user
                comment.created_at = datetime.now()
                comment.save()
                return redirect('show_article', article_id=article.id)

    return render(request, 'website/article_show.html', {
        'article': article,
        'comments': comments,
        'comment_form': comment_form
    })

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.user == article.author:
        article.delete()
        return redirect('home')
    else:
        return redirect('home')

def update_article(request, article_id):
        article = get_object_or_404(Article, id=article_id)
        if request.user == article.author:
            if request.method == 'POST':
                form = ArticleForm(request.POST, instance=article)
                if form.is_valid():
                    form.save()
                    return redirect('show_article', article_id=article.id)
            else:
                form = ArticleForm(instance=article)
            return render(request, 'website/form.html', {
                'form': form,
                'article': article
            })

        else:
            return redirect('home')

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        comment.delete()
        return redirect('show_article', article_id=comment.article.id)
    else:
        return redirect('home')

def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('show_article', article_id=comment.article.id)
        else:
            form = CommentForm(instance=comment)
        return render(request, 'website/form_comment.html', {
            'form': form,
            'comment': comment
        })
    else:
        return redirect('home')


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'website/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'website/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')




