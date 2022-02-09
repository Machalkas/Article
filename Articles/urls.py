from django.urls import path
from . import views
urlpatterns=[
    path('list/', views.ArticlesView.as_view()),
    path('<str:id>', views.ArticleView.as_view()),
    # path('edit/<str:id>', views.EditArticleView.as_view())
    ]