from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class PostListView(ListView):
    """
    A view to display a list of blog posts.
    It uses the Post model and orders the posts by creation date in descending order.
    The template name is set to 'blog/post_list.html'.
    """
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_created']

class PostDetailView(DetailView):
    """
    A view to display the details of a single blog post.
    It uses the Post model and the template name is 'blog/post_detail.html'.
    """
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    A view to create a new blog post.
    It requires the user to be logged in to access the view.
    It uses the Post model and the template name is 'blog/post_form.html'.
    The fields 'title', 'content', and 'author' are included in the form.
    Upon successful form submission, it redirects to the post list view.
    """
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('blog:blog_index')

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    A view to update an existing blog post.
    It requires the user to be logged in and to be the author of the post to update it.
    It uses the Post model and the template name is 'blog/post_form.html'.
    The fields 'title', 'content', and 'author' are included in the form.
    Upon successful form submission, it redirects to the post detail view.
    """
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'author']
    
    def test_func(self):
        """
        Check if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    A view to delete an existing blog post.
    It requires the user to be logged in and to be the author of the post to delete it.
    It uses the Post model and the template name is 'blog/post_confirm_delete.html'.
    Upon successful form submission, it redirects to the post list view.
    """
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:blog_index')
    
    def test_func(self):
        """
        Check if the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author
