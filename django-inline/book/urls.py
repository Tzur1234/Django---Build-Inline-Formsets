
from django.urls import path, include
from . import views


app_name = 'books'
urlpatterns = [
    path('', views.HomeView.as_view(), name='books')
]