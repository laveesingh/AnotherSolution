import datetime

from django import forms

from pagedown.widgets import PagedownWidget
from froala_editor.widgets import FroalaEditor

from .models import Post


class PostForm(forms.ModelForm):

    body = forms.CharField(
        widget=FroalaEditor
    )
    date = forms.DateField(widget=forms.SelectDateWidget)
    last_edit_date = forms.DateField(widget=forms.SelectDateWidget, initial=datetime.date.today)
    
    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "body",
            "tags",
            "date",
            "last_edit_date",
        ]