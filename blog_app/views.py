from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView)
from . import models
from blog_app.forms import UserForm

class BlogIndexView(TemplateView):
    template_name = 'blog_app_index.html'

class BlogRegisterView(TemplateView):
    context_object_name = 'user_form'
    template_name = 'blog_app_register.html'

class BlogListView(ListView):
    model = models.BlogPost
    template_name = 'blog_app_list.html'

class BlogDetailView(DetailView):
    context_object_name = 'blogpost_detail'
    model = models.BlogPost
    template_name = 'blog_detail.html'

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data = request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'blog_app_register.html', {'user_form': user_form,
                                                     'registered': registered})
