from django import forms
from .models import UserPost

class PostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ('title','body','author')

        widgets = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'author':forms.TextInput(attrs={'class':'textinputclass'}),
        'body':forms.Textarea(attrs={'class':'postcontent'})
        }