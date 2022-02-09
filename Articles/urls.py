from django.urls import path
from . import views
urlpatterns=[
path('get/', views.ArticleViewSet.as_view())
]