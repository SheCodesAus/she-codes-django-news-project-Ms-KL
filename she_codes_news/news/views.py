# -------------- NOTE ORIGINAL SETUP CODE
# -------------- COMMENTED OUT FOR SAFETY

# # FORMS SETUP Step 1: add a view to use the form
# from django.views import generic
# from django.urls import reverse_lazy #added
# from .models import NewsStory
# from .forms import StoryForm #added

# class IndexView(generic.ListView):
#     template_name = 'news/index.html'

#     def get_queryset(self):
#         '''Return all news stories.'''
#         return NewsStory.objects.all()
#         #  get all news stories and use in index

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['latest_stories'] = NewsStory.objects.all()[:4]
#         # ['latest_stories'] = like slicing. Just use first 4 stories [:4]
#         context['all_stories'] = NewsStory.objects.all()
#         return context

# # SETUP NEWS Step 13: Add a view for a single story
# class StoryView(generic.DetailView):
#     model = NewsStory
#     template_name = 'news/story.html'
#     context_object_name = 'story'

# # FORMS SETUP Step 1: add a view to use the form
# class AddStoryView(generic.CreateView):
#     form_class = StoryForm
#     context_object_name = 'storyForm'
#     template_name = 'news/createStory.html'
#     success_url = reverse_lazy('news:index')

# # USERS SETUP Step 12:  update the view to complete the author field
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

# # referred to urls.py
# # class based view (part 4 in tutorial)
#     # can use function based view
#     # similar, but looks different

# -------------- ASSIGNMENT CODE -------------

# FORMS SETUP Step 1: add a view to use the form
from django.views import generic
from django.urls import reverse_lazy #added
from .models import NewsStory
from .forms import StoryForm #added

class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        #  get all news stories and use in index
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ---- ASSIGNMENT PART 1: Order the stories by date
        stories = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = stories[:4]
        # display all stories from after the last "latest_story" is displayed
        context['all_stories'] = stories[4:]
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

    # USERS SETUP Step 12:  update the view to complete the author field
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# ---- ASSIGNMENT PART 1: Order the stories by date
            # add ordering to models - refer to this in views
            # https://medium.com/@thexovc/how-to-order-blogpost-in-django-53218db7b092
            # doesn't work:
            # return NewsStory.objects.all.order_by('-pub_date')
        # https://docs.djangoproject.com/en/4.0/intro/tutorial03/
        # latest_story_list = NewsStory.objects.order_by('-pub_date')
        # context = {'latest_story_list': latest_story_list}
        # return render(self,'news/index.html', context)
        # # KG NOTE this uses import render and import NewsStory

# NOTE
# referred to urls.py
# class based view (part 4 in tutorial)
    # can use function based view
    # similar, but looks different