from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment

# -----------------------
# STORY BLOCK
class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['pub_date','title','image_field', 'content' ]
        labels = {
            'title': ('Story Title'),
            'pub_date': ('Date Published'),
            'image_field': ('Image URL'),
            'content': ('Write a Story'),
        }
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'},),
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={
                'placeholder':'Select a date', 
                'type':'date', }),
            'image_field':forms.URLInput(attrs={'class':'form-control'},),
            }

# -----------------------
# COMMENT BLOCK
class CommentForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = ""
    class Meta:
        model = Comment
        fields = ["content"]



# -----------------------
    # REFERENCES:
        # https://djangocentral.com/creating-comments-system-with-django/
        # https://www.youtube.com/watch?v=0x0pWrm2nKI
        # https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
        # https://studygyaan.com/django/django-style-the-forms-created-by-model-forms
        # https://colinkingswood.github.io/Model-Form-Customisation/
        # https://medium.com/swlh/how-to-style-your-django-forms-7e8463aae4fa
        # https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
        # https://docs.djangoproject.com/en/4.0/ref/forms/fields/#imagefield


    # ALTERNATIVE SOLUTIONS:
    # {% comment %}

        # ALTERNATIVE 1: Import Custom User for Author Dropdown
            # from users.models import CustomUser
            # class AuthorForm (forms.Form):
            #     customuser = forms.ModelChoiceField(queryset=CustomUser.objects.all()

        # ALTERNATIVE 2: Story Form
            # class StoryForm(ModelForm):
            #     class Meta:
            #         model = NewsStory
            #         fields = ['pub_date','title','image_field', 'content' ]
            #         # author 
            #         labels = {
            #             'title': ('Blog Title'),
            #             'pub_date': ('Date Published'),
            #             'image_field': ('Image URL'),
            #             'content': ('Write your Blog'),
            #         }
            #         widgets = {
            #             'title':forms.TextInput(attrs={'class':'form-control'},),
            #             'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={
            #                 'class':'form-control', 
            #                 'placeholder':'Select a date', 
            #                 'type':'date', }),
            #             'image_field':forms.URLInput(attrs={'class':'form-control'},),
            #             }
        
        # OG CODE FROM SETUP:
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
        
    # {% endcomment %}