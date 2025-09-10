from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm

class PostDetailView(DetailView):
    """
    View to display a single blog post and handle new comment submissions.
    """
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add the comment form to the context for display
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        """
        Handles the creation of a new comment.
        """
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a new comment instance but don't save yet
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = self.request.user
            comment.save()
            return redirect('blog:post_detail', slug=self.object.slug)
        else:
            # If the form is invalid, re-render the page with the form and errors
            context = self.get_context_data()
            context['form'] = form  # Pass the form with errors
            return render(request, self.template_name, context)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for authenticated users to edit their own comments.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_update.html'

    def get_success_url(self):
        # Redirect to the post detail page after a successful update
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.post.slug})

    def test_func(self):
        # Ensure the user is the author of the comment
        comment = self.get_object()
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    View for authenticated users to delete their own comments.
    """
    model = Comment
    template_name = 'blog/comment_delete.html'

    def get_success_url(self):
        # Redirect to the post detail page after a successful delete
        return reverse_lazy('blog:post_detail', kwargs={'slug': self.object.post.slug})

    def test_func(self):
        # Ensure the user is the author of the comment
        comment = self.get_object()
        return self.request.user == comment.author
