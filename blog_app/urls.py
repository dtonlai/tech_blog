from django.conf.urls import url
from . import views

app_name = 'tech_blog'

urlpatterns = [
    url(r'^$', views.BlogListView.as_view()),
    url(r'^(?P<pk>\d+)/$', views.BlogDetailView.as_view()),
]
