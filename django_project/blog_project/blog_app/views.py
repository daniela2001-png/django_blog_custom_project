from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .models import Post


class PostListView(ListView):
    """
    class-based view that lists posts from an user
    """
    
    model = Post
    template_name = "blog_app/home.html"
    context_object_name = 'posts'
    ordering = ['-date_posted'] # order by date_posted in a desc way


class PostDetailView(DetailView):
    """
    class-based view that shows the details of a post from an user
    """
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """
    class-based view that creates a new post
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        If the form is valid, sets the associated current user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    """
    class-based view that updates an existing post
    """
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        If the form is valid, sets the associated current user
        """
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool:
        """
        Deny a request with a permission error if the test_func() method returns False.
        
        Return: A boolean that indicates if the current_user can updates a blog post.
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    """
    class-based view that deletes a post from an user
    """
    model = Post
    success_url = '/' # if the post is deleted correctly, we redirect successfully to the home page


    def test_func(self) -> bool:
        """
        Deny a request with a permission error if the test_func() method returns False.
        
        Return: A boolean that indicates if the current_user can updates a blog post.
        """
        post = self.get_object()
        return self.request.user == post.author




def home(request) -> HttpResponse:
    context = {
        "posts": Post.objects.all()
    }
    return render(request, "blog_app/home.html", context)


def about(request) -> HttpResponse:
    return render(request, "blog_app/about.html", {"title": "about"})