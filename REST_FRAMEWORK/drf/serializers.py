from rest_framework import serializers
from .models import Snippet
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    model = User
    fields = ['id', 'username', 'snippets']


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
