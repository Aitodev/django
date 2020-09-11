from django.shortcuts import render
from .models import Post


def hello(request):
    post = Post.objects.all()
    return render(request, 'app/index.html', context={'posts': post})
