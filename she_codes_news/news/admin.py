from django.contrib import admin

# Register your models here.
# https://docs.djangoproject.com/en/4.1/intro/tutorial07/#customize-the-admin-form

from .models import NewsStory

class NewsStoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Story Data',       {'fields': ['title']}),
        (None,               {'fields': ['author']}),
        (None,               {'fields': ['pub_date']}),
        ('Story Content',    {'fields': ['image_field']}),
        (None,               {'fields': ['content']}),
    ]
    list_display = ('title', 'pub_date')

admin.site.register(NewsStory, NewsStoryAdmin)