from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post


class PostForm(forms.ModelForm):

    body = forms.CharField(widget=PagedownWidget)
    date = forms.DateField(widget=forms.SelectDateWidget)
    
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "tags",
            "date",
        ]