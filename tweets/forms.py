from django import forms
from django.conf import settings
from django.db.models.base import Model
from django.forms import fields
from .models import Tweet


MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH


class TweetForm(forms.ModelForm):
    class  Meta:
        model=Tweet
        fields=['content']

    def clean_content(self):
        content=self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This Tweet is too long")
        return content
