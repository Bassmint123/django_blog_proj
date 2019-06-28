from django.urls import path

from .views import BlogListView, BlogDetailView 

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # see the details of each blog post
    path('', BlogListView.as_view(), name='home'),
]