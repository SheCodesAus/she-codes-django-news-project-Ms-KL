from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['pub_date','title','image_field', 'content' ]
        # USER SETUP: Step 12 Removed 'author'
        labels = {
            'title': ('Blog Title'),
            'pub_date': ('Date Published'),
            'image_field': ('Image URL'),
            'content': ('Write your Blog'),
        }
        # FORMS SETUP Step 2: add a date picker widget
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'},),
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={
                # 'class':'form-control', 
                'placeholder':'Select a date', 
                'type':'date', }),
            'image_field':forms.URLInput(attrs={'class':'form-control'},),
            }

#COMMENT
#https://djangocentral.com/creating-comments-system-with-django/
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenter_name', 'comment_email', 'comment_body']
        labels = {
            'commenter_name':('Name'), 
            'comment_email': ('Email'), 
            'comment_body':('Write your Comment'),
        }

# -----------------------------------------------------------------------------

# ___ ASSIGNMENT PART 1: STYLE THE FORM FOR ADDING NEW STORIES
    # KG DO:
        # add widget items
        # assign class to widget items to reference in css
        # update label names for UX
        # format as table in HTML
        # update CSS
            # fix alignment so fields are even and aligned (using table) 

# ---------------------

# ___ REFERENCES:
    # https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
    # https://studygyaan.com/django/django-style-the-forms-created-by-model-forms
    # https://colinkingswood.github.io/Model-Form-Customisation/
    # https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
    # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
    # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#imagefield

# ---------------------

# ___ NOTE ORIGINAL CODE
    # # FORMS SETUP Step 1: create forms.py and add:
    #     # What are we supposed to enter for the data? 
    #     # We’ll fix that using a widget in the next step.

    # from django import forms
    # from django.forms import ModelForm
    # from .models import NewsStory
    # class StoryForm(ModelForm):
    #     class Meta:
    #         model = NewsStory
    #         fields = ['title', 'pub_date', 'content']
    #         # USER SETUP: Step 12 Removed 'author'
    #         # FORMS SETUP Step 2: add a date picker widget
    #         widgets = {
    #             'pub_date': forms.DateInput(format=('%m/%d/%Y'),
    #             attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date',}),
    #             }