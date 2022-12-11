from django.contrib.auth import get_user_model #ADDED
from django.db import models




# -----------------------
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_field = models.URLField(blank=True) #ADDED
    # default='https://ms-kl.github.io/images/shecodes-icon.png'

    # define to blog list in admin portal
    def __str__(self):
        return self.title





# -----------------------
# comment - HELP!!!!
# https://djangocentral.com/creating-comments-system-with-django/
class Comment(models.Model):
    comment_post = models.ForeignKey(NewsStory,on_delete=models.CASCADE,related_name='comments')
    commenter_name = models.CharField(max_length=80)
    comment_email = models.EmailField()
    comment_body = models.TextField()
    comment_created_on = models.DateTimeField(auto_now_add=True)
    comment_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['comment_created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.comment_body, self.commenter_name)







# -----------------------------------------------------------------------------

# __ ASSIGNMENT PART 1:
    # Add a field to the NewsStory model for an image url and 
    # use this image url rather than the default images provided in the starter

# ---------------------

# __ NOTE: 
    # Textfield for no max length
    # properties: title, author, pub_date
    # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
    # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#imagefield
    # must set default or URL field won't work

# ---------------------

# __ ORIGINAL CODE TO CHANGE:
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
