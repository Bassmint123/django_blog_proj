from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView  # added the DetailView for individual blog pages
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_detail.html'
