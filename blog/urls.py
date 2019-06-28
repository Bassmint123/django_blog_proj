from django.urls import path

from .views import (BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView) 

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # see the details of each blog post
    path('', BlogListView.as_view(), name='home'),
]