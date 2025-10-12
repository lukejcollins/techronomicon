from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from markdownx.utils import markdownify

from .models import AboutPage, Post


def home(request):
    posts = Post.objects.order_by('-pub_date')

    for post in posts:
        post.content = markdownify(post.get_truncated_content())

    return render(request, 'techronomiblog/home.html', {'posts': posts})


def about(request):
    about_page = AboutPage.objects.first()
    about_page.content = markdownify(about_page.content)
    ctx = {"about_page": about_page}
    return render(request, "techronomiblog/about.html", ctx)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.content = markdownify(post.content)
    return render(request, 'techronomiblog/post_detail.html', {'post': post})


def health(_request):
    return HttpResponse("ok")
