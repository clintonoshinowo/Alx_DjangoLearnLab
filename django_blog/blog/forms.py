from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    A form for creating and updating comments.
    """
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': 'Your Comment',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Type your comment here...'}),
        }
