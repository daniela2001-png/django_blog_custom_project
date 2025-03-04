from django.urls import path
from . import views

# list of views for blog_app application
urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about")
]
