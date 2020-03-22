from django import forms
from .models import Topic, Post


class TopicForm(forms.ModelForm):

    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5,
        'placeholder': 'fill this message'
    }), max_length=2000, help_text='please fill it nicely....')

    class Meta:
        model = Topic
        fields = ['subject', 'message']


class ReplyForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['message']
