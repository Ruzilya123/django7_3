from django.shortcuts import render
from .forms import Form
from .models import Post
from rest_framework import generics
from .models import Post
from .serializers import SnippetSerializerV2


class SnippetListV3(generics.ListCreateAPIView):
    queryset = Post.objects.all() # 
    serializer_class = SnippetSerializerV2


class SnippetDetailV3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = SnippetSerializerV2

