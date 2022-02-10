from django.urls import path
from . import views

urlpatterns=[
    path('register/', views.UserRegisterView.as_view()),
    path('self/', views.SelfView.as_view()),
    path('<int:id>/', views.UserView.as_view())
    ]