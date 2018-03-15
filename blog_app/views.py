from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView,
                                DetailView, CreateView, UpdateView,
                                DeleteView)
from . import models

class BlogIndexView(TemplateView):
    template_name = 'blog_app_index.html'

class BlogListview(ListView):
    template_name = 'blog_app_list.html'
    model = models.BlogPost
