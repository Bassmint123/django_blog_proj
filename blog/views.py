from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView  # added the views for individual blog pages
from django.views.generic.edit import CreateView, UpdateView, DeleteView # using the generic edit for creating a new post
# We use reverse_lazy as opposed to just reverse so that it won’t execute the URL
# redirect until our view has finished deleting the blog post.
from django.urls import reverse_lazy # new

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']	

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')