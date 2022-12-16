from django.views import generic
from django.urls import reverse_lazy 
from news.models import NewsStory 
from .forms import StoryForm, CommentForm
from django.shortcuts import render, get_object_or_404
from users.models import CustomUser 
from django.contrib.auth.decorators import login_required

# -----------------------
# INDEX BLOCK (NEWS)
class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        #  get all news stories and use in index
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stories = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = stories[:4]
        # display all stories from after the last "latest_story" is displayed
        context['all_stories'] = stories[4:]
        return context

# -----------------------
# EXPLORE BLOCK
class ExploreView(generic.ListView):
    model = CustomUser
    template_name = 'news/exploreStories.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()
    
    def get_queryset(self):
        '''Return all authors of stories.'''
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['story_authors'] = CustomUser.objects.all()
        return context

# -----------------------
# STORY BLOCK - SINGLE STORY
class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["form_action"] = reverse_lazy("news:addComment", kwargs={"pk": self.kwargs.get('pk')})
        return context


# -----------------------
# ADDSTORY BLOCK
class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# -----------------------
# ADDCOMMENT BLOCK
class AddCommentView(generic.CreateView):
    form_class = CommentForm
    success_url = reverse_lazy("news:newsStory")
    template_name = 'news/createComment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})

# -----------------------
# EDITSTORY BLOCK

class EditStoryView(generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'story'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy("news:newsStory")

    def form_valid(self, form):
        """Save the form and redirect to the success URL."""
        # Save the updated form
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form) 

    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})



class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    context_object_name = 'story'
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')



# -----------------------
    # FUNCTION:
    # <INSERT>

    # ASSIGNMENT:
    # <INSERT>

    # REFERENCES:
    # https://medium.com/@thexovc/how-to-order-blogpost-in-django-53218db7b092
    # https://docs.djangoproject.com/en/4.0/intro/tutorial03/
    # https://shecodesaus.slack.com/archives/CLE9UP5QD/p1670635169787339
    # https://www.youtube.com/watch?v=xNV4GFgRCUE
    # https://docs.djangoproject.com/en/4.0/ref/class-based-views/generic-editing/#formview
    # Which Django generic to use for which job?
        # generic.ListView for when you want to see all (or a subset) of a models data
        # generic.DetailView for when you want one specific item from a model
        # edits
        # generic.edit.CreateView for when you want to create a new item in a model
        # generic.edit.UpdateView for when you want to modify one specific item from a model
        # generic.edit.DeleteView for when you want to remove one specific item from a model

    # ALTERNATIVE SOLUTIONS:
    # {% comment %}

        # ALTERNATIVE 1: ADD COMMENTS
            # def post_detail(request, slug):
            #     template_name = 'post_detail.html'
            #     post = get_object_or_404(NewsStory, slug=slug)
            #     comments = post.comments.filter(active=True)
            #     new_comment = None
            #     # Comment posted
            #     if request.method == 'POST':
            #         comment_form = CommentForm(data=request.POST)
            #         if comment_form.is_valid():

            #             # Create Comment object but don't save to database yet
            #             new_comment = comment_form.save(commit=False)
            #             # Assign the current post to the comment
            #             new_comment.post = post
            #             # Save the comment to the database
            #             new_comment.save()
            #     else:
            #         comment_form = CommentForm()

            #     return render(request, template_name, {'NewsStory': NewsStory,
            #                                            'comments': comments,
            #                                            'new_comment': new_comment,
            #                                            'comment_form': comment_form})

        # ALTERNATIVE 2: EXPLORE STORIES
            # class ExploreView(generic.ListView):
            #     template_name = 'news/exploreStories.html'

            #     def get_queryset(self):
            #         '''Return all news stories.'''
            #         return NewsStory.objects.all()

            #     def get_context_data(self, **kwargs):
            #         context = super().get_context_data(**kwargs)
            #         # ---- ASSIGNMENT PART 1: Order the stories by date
            #         context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
            #         return context

        # ALTERNATIVE 3: ADD AUTHOR DROPDOWN - PART OF EPLORE
            # def story_dropdown(request):
            #     displayauthor =NewsStory.objects.values_list('author',flat=True)
            #     # looks as NewsStory objects, puts the authors in a list to use
            #     return render(request, 'news/exploreStories.html',{"NewsStory":displayauthor})
            #     # returns a request to render displayauthor (author list from NewsStory) to explorestories.html 
            
            # def author_view(request):
            #     if request.method == 'POST':
            #         selected_author = request.POST['author']
            #     # Do something with the selected author...

        # OG CODE:
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

    # {% endcomment %}