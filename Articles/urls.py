from django.urls import path
from . import views
urlpatterns=[
path('list/', views.ArticlesViewSet.as_view()),
path('get/<str:id>', views.ArticleViewSet.as_view())

]