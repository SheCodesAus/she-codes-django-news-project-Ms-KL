# from django.shortcuts import render
# # Create your views here.


# SETUP USERS Step 9: Create view for the created account page app:

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
#added
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




# ASSIGNMENT PART 2: add an Account View
# STEPS: add Account view, add account.html, add to model? 
# class AccountView(CreateView):
#     form_class = CustomUserCreationForm# unsure what to put
#     success_url = reverse_lazy('view-account')
#     template_name = 'users/viewAccount.html'