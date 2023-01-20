from django import forms
from .models import Post, Comment, Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
