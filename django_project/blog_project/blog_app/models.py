from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    """
    Represents a post class or entity
    
    Keyword arguments:
        models.Model -- inheritance class for django models

    Class attributes:
        title -- Describes the title given for the post
        content -- Describes the content of the post
        date_posted -- Describes the datetime when the post was create (can be manually set it)
        author -- defines the foreign relationship with the existent User model from Django.
    Return: None
    """
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # default values can be overriden
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if an user is deleted their posts also will be deleted it (on_delete)

    def __repr__(self):
        return f"Post(title={self.title}, content={self.content}, date_posted={self.date_posted}, author={self.author})"

