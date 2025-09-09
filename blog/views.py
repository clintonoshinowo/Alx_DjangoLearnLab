from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

# Simple function-based view for the index page.
def index(request):
    return render(request, 'blog/index.html')

# Class-based view to display a list of all posts.
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10

# Class-based view to display a single post in detail.
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Class-based view to create a new post.
# It requires the user to be logged in and redirects to the new post's detail page on success.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Class-based view to update an existing post.
# It requires the user to be logged in and must be the author of the post.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

# Class-based view to delete a post.
# It requires the user to be logged in and must be the author of the post.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog-home')
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
