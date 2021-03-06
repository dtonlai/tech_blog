from django.shortcuts import render
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, DeleteView, UpdateView)
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from . import models
from blog_app.forms import UserForm

class BlogIndexView(TemplateView):
    template_name = 'blog_app_index.html'

class BlogRegisterView(TemplateView):
    context_object_name = 'user_form'
    template_name = 'blog_app_register.html'

@method_decorator(login_required, name='dispatch')
class BlogListView(ListView):
    model = models.BlogPost
    template_name = 'blog_app_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class BlogDetailView(DetailView):
    context_object_name = 'blogpost_detail'
    model = models.BlogPost
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView):
    fields = ('title', 'author', 'content')
    model = models.BlogPost
    template_name = 'blogpost_form.html'

class BlogUpdateView(UpdateView):
    fields = ('title', 'author', 'content')
    model = models.BlogPost
    template_name = 'blogpost_form.html'

class BlogDeleteView(DeleteView):
    model = models.BlogPost
    success_url = reverse_lazy('tech_blog:list')
    template_name = 'blogpost_confirm_delete.html'

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

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account is not active')
        else:
            print('Someone tried to login and failed')
            print('Username: {} and Password: {}'.format(username,password))
            return HttpResponse('Invalid login details!')
    else:
        return render(request, 'blog_app_login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
