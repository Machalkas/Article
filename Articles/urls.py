from django.urls import path
from . import views

urlpatterns=[
    path('list/', views.ListArticlesView.as_view()),
    path('create/', views.CreateArticleView.as_view()),
    path('<str:id>/', views.ArticleView.as_view()),
    ]