# from django.shortcuts import render
# # Create your views here.


# SETUP USERS Step 9: Create view for the created account page app:

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

# ASSIGNMENT PART 2: add an Account View
# STEPS: add Account view, add account.html, add to model? 
class AccountView(CreateView):
    form_class = CustomUserCreationForm# unsure what to put
    success_url = reverse_lazy('account')
    template_name = 'users/account.html'