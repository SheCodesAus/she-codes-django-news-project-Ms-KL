from django.contrib import admin

# Register your models here.
# https://docs.djangoproject.com/en/4.1/intro/tutorial07/#customize-the-admin-form

from .models import NewsStory, Comment

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

# COMMENT
# https://djangocentral.com/creating-comments-system-with-django/
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('commenter_name', 'comment_body', 'comment_post', 'comment_created_on', 'comment_active')
    list_filter = ('comment_active', 'comment_created_on')
    search_fields = ('commenter_name', 'comment_email', 'comment_body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)