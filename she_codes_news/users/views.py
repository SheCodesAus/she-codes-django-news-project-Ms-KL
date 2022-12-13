from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class AccountView(generic.DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
        return context



# -----------------------
    # FUNCTION:
    # <INSERT>

    # ASSIGNMENT:
    # <INSERT>

    # REFERENCES:
    # Which Django generic to use for which job?
        # generic.ListView for when you want to see all (or a subset) of a models data
        # generic.DetailView for when you want one specific item from a model
        # edits
        # generic.edit.CreateView for when you want to create a new item in a model
        # generic.edit.UpdateView for when you want to modify one specific item from a model
        # generic.edit.DeleteView for when you want to remove one specific item from a model

    # ALTERNATIVE SOLUTIONS:
    # {% comment %}

        # from django.shortcuts import render

    # {% endcomment %}