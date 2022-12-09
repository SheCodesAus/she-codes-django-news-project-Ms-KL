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
    image_field = models.URLField(default='https://cdn.pixabay.com/photo/2022/11/29/16/34/bird-7624853_960_720.jpg')
    # must set default or field won't work

# NOTE 
# Textfield for no max length
# properties: title, author, pub_date
# https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
# https://docs.djangoproject.com/en/4.0/ref/forms/fields/#imagefield

# default:
# https://pixabay.com/photos/bird-sparrow-songbird-feathers-7624853/
