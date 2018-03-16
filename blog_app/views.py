from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from . import models

class BlogIndexView(TemplateView):
    template_name = 'blog_app_index.html'

class BlogListView(ListView):
    model = models.BlogPost
    template_name = 'blog_app_list.html'

class BlogDetailView(DetailView):
    context_object_name = 'blogpost_detail'
    model = models.BlogPost
    template_name = 'blog_detail.html'
