from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.contrib import messages
from .models import Author


class HomeView(TemplateView):
    template_name = 'home.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name']

    # FormMixin parentcClass
    # Retrieve initial data for the form. By default, returns a copy of initial.
    # def get_initial(self, *args, **kwargs):
    #     initial = super().get_initial(**kwargs)
    #     initial['name'] = "Enrer Author's name"
    #     return initial

    def form_valid(self, form):
        messages.success(self.request, 'The author has been added!')
        return super().form_valid(form)

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorBooksEditView(UpdateView):
    model = Author
    fields = ['name']
    template_name = 'author_update.html'




















