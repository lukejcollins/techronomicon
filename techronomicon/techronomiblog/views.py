from django.shortcuts import render
from .models import Post
from markdownx.utils import markdownify

def home(request):
    posts = Post.objects.order_by('-pub_date')
    
    # Convert Markdown content to HTML for each post
    for post in posts:
        post.content = markdownify(post.content)
    
    return render(request, 'techronomiblog/home.html', {'posts': posts})

def about(request):
    return render(request, 'techronomiblog/about.html')

