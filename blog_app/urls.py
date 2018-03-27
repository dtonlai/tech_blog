from django.conf.urls import url
from . import views

app_name = 'tech_blog'

urlpatterns = [
    url(r'^$', views.BlogListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', views.BlogDetailView.as_view(), name='detail'),
    url(r'^create/$', views.BlogCreateView.as_view(), name='create'),
    url(r'^update/(?P<pk>\d+)$', views.BlogUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)$', views.BlogDeleteView.as_view(), name='delete'),
]
