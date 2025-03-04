from django.urls import path
from .views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

# list of views for blog_app application
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new', PostCreateView.as_view(), name="post-creation"),
    path('about/', views.about, name="blog-about")
]
