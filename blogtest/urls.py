"""
URL configuration for blogtest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index_articles, name='home'),
    path('add/', views.article_form_view, name='article'),
    path('article/<int:article_id>/', views.show_article, name='show_article'),
    path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('article/edit/<int:article_id>/', views.update_article, name='update_article'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('comment/edit<int:comment_id>/', views.update_comment, name='update_comment'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
