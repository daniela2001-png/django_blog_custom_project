from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    """
    Represents a profile class or entity
    
    Keyword arguments:
        models.Model -- inheritance class for django models

    Class attributes:
        user -- Describes the one-to-one relationship with the User model
        image -- Represents the picture profile of the user
    Return: None
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE) # creates a one-to-one relationship with the User model
    image = models.ImageField(default='default.jpg', upload_to='profile_pics') # loads the images at the relative path profile_pics

    def __repr__(self) -> str:
        """represents a profile instance
        
        Return: A profile representation
        """
        
        return f"Profile(username={self.user.username})"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        # resize image to 300 px x 300 px
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

