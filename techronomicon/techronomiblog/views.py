from django.shortcuts import render
from .models import Post
from markdownx.utils import markdownify
from django.shortcuts import render, get_object_or_404

def home(request):
    posts = Post.objects.order_by('-pub_date')
    
    # Convert Markdown content to HTML for each post
    for post in posts:
        post.content = markdownify(post.get_truncated_content())
    
    return render(request, 'techronomiblog/home.html', {'posts': posts})

def about(request):
    return render(request, 'techronomiblog/about.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.content = markdownify(post.content)
    return render(request, 'techronomiblog/post_detail.html', {'post': post})
