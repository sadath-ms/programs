from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^mac/$', views.Post_ListView.as_view(), name='list_view'),
    url(r'^mac/about/$', views.AboutView.as_view(), name='about_view'),
    url(r'^mac/detail/(?P<pk>\d+)$', views.Post_DetailView.as_view(), name='detail'),
    url(r'^mac/detail/new/$', views.Post_CreateView.as_view(), name='create'),
    url(r'^mac/detail/(?P<pk>\d+)/edit/$', views.Post_UpdateView.as_view(), name='update'),
    url(r'^mac/detail/(?P<pk>\d+)/remove/$', views.Post_DeleteView.as_view(), name='delete'),
    url(r'^mac/draft/$', views.DraftListView.as_view(), name='draft')
    ] 
