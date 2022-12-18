
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    def __str__(self):
        return self.username

# -----------------------

        # ALTERNATIVE 1:
        # class CustomUser(AbstractUser):
            # profile_image = models.URLField(blank=True)
            # KG: Users comes with Django
            # KG: Write custom user class, use the inbuilt User function and abstract to inherit the user functions and build on it
            # pass

    # {% endcomment %}