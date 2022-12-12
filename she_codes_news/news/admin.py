from django.contrib import admin
from .models import NewsStory, Comment

# -----------------------
# NEWSSTORY BLOCK
class NewsStoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Story Data',       {'fields': ['title']}),
        (None,               {'fields': ['author']}),
        (None,               {'fields': ['pub_date']}),
        ('Story Content',    {'fields': ['image_field']}),
        (None,               {'fields': ['content']}),
    ]
    list_display = ('title','author', 'pub_date')

admin.site.register(NewsStory, NewsStoryAdmin)

# -----------------------
# ADMIN BLOCK
class CommentAdmin(admin.ModelAdmin):
    list_display = ('story', 'author', 'content', 'created_at', 'modified_at')
    list_filter = ('created_at','story')
    search_fields = ('author', 'content','story')

admin.site.register(Comment, CommentAdmin)


# -----------------------
    # FUNCTION:
    # <INSERT>

    # ASSIGNMENT:
        # <INSERT>

    # REFERENCES:
        # https://youtu.be/SImJVdZocvQ
        # https://djangocentral.com/creating-comments-system-with-django/
        # https://docs.djangoproject.com/en/4.1/intro/tutorial07/#customize-the-admin-form

    # ALTERNATIVE SOLUTIONS:
    # {% comment %}

        # ALTERNATIVE 1: Admin Register (Ben)
            # from . import models
            # admin.site.register(models.Comment)
        
        # ALTERNATIVE @: Admin Register
            # @admin.register(Comment)
            # class CommentAdmin(admin.ModelAdmin):
            #     list_display = ('commenter_name', 'comment_body', 'comment_post', 'comment_created_on', 'comment_active')
            #     list_filter = ('comment_active', 'comment_created_on')
            #     search_fields = ('commenter_name', 'comment_email', 'comment_body')
            #     actions = ['approve_comments']

            #     def approve_comments(self, request, queryset):
            #         queryset.update(active=True)

    # {% endcomment %}