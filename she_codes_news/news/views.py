from django.views import generic
from .models import NewsStory


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()
        #  get all news stories and use in index

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        # ['latest_stories'] = like slicing. Just use first 4 stories [:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

# SETUP NEWS Step 13: Add a view for a single story
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# NOTE
# referred to urls.py
# class based view (part 4 in tutorial)
    # can use function based view
    # similar, but looks different
# 