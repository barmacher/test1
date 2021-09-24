from rest_framework import serializers
from django import forms

from .models import Blog


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    image = forms.ImageField(required=True)
    description = forms.CharField(max_length=1000)
    hashtags = forms.CharField(max_length=100)



class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "image",
            "title",
            "description",
            "hashtags"
        ]
        # def validate(self,attrs):


