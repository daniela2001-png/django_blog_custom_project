from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request) -> HttpResponse:
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog_app/home.html", context)


def about(request) -> HttpResponse:
    return render(request, "blog_app/about.html", {"title": "about"})