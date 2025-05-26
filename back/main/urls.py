from django.urls import path
from main import views

urlpatterns = [
    path('/t', views.Hello, name='index'),
]