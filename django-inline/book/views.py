from django.shortcuts import render
from django.urls import reverse
# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from .models import Author
from .forms import AuthorBooksFormset


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


# class AuthorBooksEditView(UpdateView):
#     model = Author
#     fields = ['name']
#     template_name = 'author_update.html'

class AuthorBooksEditView(SingleObjectMixin, FormView):
    model = Author
    template_name = 'author_update.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Author.objects.all())
        return super().post(request, *args, **kwargs)
    
    def get_form(self, form_class=None):
        return AuthorBooksFormset(**self.get_form_kwargs(), instance=self.object)


    #Validation
    def form_valid(self, form):
        # Excplicitly save the form in the data
        form.save()
        # Add new messsage
        messages.success(self.request, 'The auther has been Update successfuly !')
        return HttpReponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('books:author_detail')

















