# -------------- NOTE ORIGINAL SETUP CODE
# -------------- COMMENTED OUT FOR SAFETY

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

# -------------- ASSIGNMENT CODE

from django import forms
from django.forms import ModelForm
from .models import NewsStory
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image_field']
        # USER SETUP: Step 12 Removed 'author'
        # FORMS SETUP Step 2: add a date picker widget
        # ASSIGNMENT PART 1: STYLE THE FORM FOR ADDING NEW STORIES
        # https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
        # https://studygyaan.com/django/django-style-the-forms-created-by-model-forms
        # https://colinkingswood.github.io/Model-Form-Customisation/
        # https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
        # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#imagefield
        # TODO styling

        # --- added labels
        labels = {
            'title': ('Blog Title'),
            'pub_date': ('Date Published'),
            'content': ('Write your Blog'),
            'image_field': ('Image URL'),
        }

        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={
                'class':'form-control', 
                'placeholder':'Select a date', 
                'type':'date',}),
            }