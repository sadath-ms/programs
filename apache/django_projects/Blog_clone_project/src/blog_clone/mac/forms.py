from django import forms
from mac.models import Post,Comments

class PostForm(forms.ModelForm):
    """Django ModelForm for model Post"""
    class Meta:
        model = Post
        fields = ['author','title','text']

        widgets={
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Tettarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }



class CommentForm(forms.ModelForm):
    """Django ModelForm for model NAME"""
    class Meta:
        model = Comments
        fields = ['author','text']

        widgets={
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Tettarea(attrs={'class':'editable medium-editor-textarea'})
        }
