from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # URL for viewing a single post and creating a new comment.
    # The 'post' method in PostDetailView handles the comment creation.
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    
    # URL for creating a new comment on a specific post.
    path('post/<slug:slug>/comments/new/', views.CommentCreateView.as_view(), name='comment_new'),

    # URL for updating an existing comment.
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),

    # URL for deleting an existing comment.
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]
