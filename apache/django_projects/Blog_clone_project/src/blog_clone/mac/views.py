from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.mixins import LoginRequiredMixins
from mac.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.views.generic import (
                                    TemplateView,
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView,

)

from mac.models import Post,Comments

class AboutView(TemplateView):
    template_name = 'about.html'


class Post_ListView(ListView):
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))



class Post_DetailView(DetailView):
    model=Post


class Post_CreateView(LoginRequiredMixins,CreateView):
    login_url='/login/'
    redirect_field_names='blog/details.html'
    form_class= PostForm
    model=Post


class Post_UpdateView(LoginRequiredMixins,UpdateView):
    login_url='/login/'
    redirect_field_names='blog/details.html'
    form_class= PostForm
    model=Post


class Post_DeleteView(LoginRequiredMixins,DeleteView):
    model=Post
    success_url=reverse_lazy('list_view')



class DraftListView(LoginRequiredMixins,ListView):
    login_url='/login/'
    redirect_field_names='blog/list.html'
    model=Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=True).order_by('create_date')
        
