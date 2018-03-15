from django.shortcuts import render
from django.views.generic import (View, TemplateView,)

class IndexView(TemplateView):
    template_name = 'blog_app_index.html'

# Create your views here.
