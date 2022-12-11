# SETUP USERS Step 2: Create the new user model

from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # profile_image = models.URLField(blank=True)
    # KG: Users comes with Django
    # KG: Write custom user class, use the inbuilt User function and abstract to inherit the user functions and build on it
    # pass

    def __str__(self):
        return self.username
    
    # KG: override the dunder to return the name of the user instead of the ID

    # add profile picture