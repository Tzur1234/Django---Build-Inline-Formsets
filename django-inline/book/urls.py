
from django.urls import path, include
from . import views


app_name = 'books'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/add/', views.AuthorCreateView.as_view(), name='add_author'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(),name='author_detail'),
    path('authors/<int:pk>/books/edit', views.AuthorBooksEditView.as_view(),name='author_book_edit')
]