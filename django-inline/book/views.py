from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView

from .models import Author


class HomeView(TemplateView):
    template_name = 'home.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorCreateView(CreateView):
    pass










