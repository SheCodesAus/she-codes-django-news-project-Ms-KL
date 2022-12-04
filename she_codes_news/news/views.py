# FORMS SETUP Step 1: add a view to use the form
from django.views import generic
from django.urls import reverse_lazy #added
from .models import NewsStory
from .forms import StoryForm #added

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

# FORMS SETUP Step 1: add a view to use the form
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

# NOTE
# referred to urls.py
# class based view (part 4 in tutorial)
    # can use function based view
    # similar, but looks different