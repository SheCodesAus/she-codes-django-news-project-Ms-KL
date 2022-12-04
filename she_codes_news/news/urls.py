from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # NEWS SETUP Step 13: Use the view (for single story) in the URLS
    path('<int:pk>/', views.StoryView.as_view(), name='story')
]

# KG: NOTE
# only 1 URL setup: index referring to views