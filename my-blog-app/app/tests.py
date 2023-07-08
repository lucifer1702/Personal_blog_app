from django.test import TestCase
from app.models import Post
# Create your tests here.
from django.shortcuts import render

def post_page(request,slug):
    post=Post.objects.get(slug=slug)
    context={'post':post}
    return render(request,'app/post.html',)

