from django import forms
from .models import Note , Comment
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

class AddNote(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget() )
    class Meta:
        model = Note
        fields = ['title', 'content', 'tags','img','active']


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
