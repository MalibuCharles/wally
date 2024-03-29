from tkinter import Widget
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            # 'author': forms.HiddenInput(), 
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }

class Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            # 'author': forms.HiddenInput(),
            'body': forms.Textarea(attrs={'class': 'form-control'}),

        }