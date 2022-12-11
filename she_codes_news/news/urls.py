from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # NEWS SETUP Step 13: Use the view (for single story) in the URLS
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    # FORMS SETUP Step 1: add form to the urls
    # What are we supposed to enter for the data? 
    # We’ll fix that using a widget in the next step.
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
]