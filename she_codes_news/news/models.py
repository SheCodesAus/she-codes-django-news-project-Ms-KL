from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


# -----------------------
# NEWSTORY BLOCK
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        USER, on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_field = models.URLField(blank=True)

    # display blog title in admin portal on list
    def __str__(self):
        return self.title

# -----------------------
# COMMENT BLOCK
# https://youtu.be/SImJVdZocvQ
class Comment(models.Model):
    story = models.ForeignKey(NewsStory,on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(
        USER, related_name="comments", on_delete=models.CASCADE, null=True,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.story


# -----------------------
    # FUNCTION:
    # <INSERT>

    # ASSIGNMENT:
    # <INSERT>

    # REFERENCES:
    # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
    # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#imagefield
    # must set default or URL field won't work
    # Textfield for no max length

    # ALTERNATIVE SOLUTIONS:
    # {% comment %}

        # OG CODE:
            # # SETUP USERS Step 10: use the user as the author
            # from django.contrib.auth import get_user_model
            # from django.db import models

            # class NewsStory(models.Model):
            #     title = models.CharField(max_length=200)
            #     # author = models.CharField(max_length=200)
            #     # SETUP USERS Step 10: use the user as the author
            #     author = models.ForeignKey(
            #         get_user_model(),
            #         # KG: use custom user class we created
            #         on_delete=models.CASCADE
            #     )
            #     pub_date = models.DateTimeField()
            #     content = models.TextField()

    # {% endcomment %}