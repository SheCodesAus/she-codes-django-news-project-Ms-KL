# FORMS SETUP Step 1: create forms.py and add:
    # What are we supposed to enter for the data? 
    # We’ll fix that using a widget in the next step.

from django import forms
from django.forms import ModelForm
from .models import NewsStory
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content']
        # USER SETUP: Step 12 Removed 'author'
        # FORMS SETUP Step 2: add a date picker widget
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            }

