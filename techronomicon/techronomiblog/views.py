from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.order_by('-pub_date')
    return render(request, 'techronomiblog/home.html', {'posts': posts})
