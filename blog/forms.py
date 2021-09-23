from rest_framework import serializers
from django import forms

from .models import Blog


class BlogForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField()
    hashtags = forms.CharField()


class BlogSerializer(serializers.ModelSerializer):


        model = Blog
        id = serializers.IntegerField(required=True)
        image = serializers.ImageField(required=True)
        tittle = serializers.CharField(required=True)
        description = serializers.CharField(required=True)
        hashtags = serializers.CharField(required=True)
        # def validate(self,attrs):


