# SETUP USERS Step 10: use the user as the author
from django.contrib.auth import get_user_model
from django.db import models



class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    # SETUP USERS Step 10: use the user as the author
    author = models.ForeignKey(
        get_user_model(),
        # KG: use custom user class we created
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()

# NOTE 
# Textfield for no max length
# properties: title, author, pub_date
