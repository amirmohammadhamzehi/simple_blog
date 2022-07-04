from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

class BlogListView(ListView):
    model = Post
    template_name = 'blog_app/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_app/post_new.html'
    fields = ['title', 'auther', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_app/post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_app/post_delete.html'
    success_url = reverse_lazy('home')