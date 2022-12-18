from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('explore-all-stories/', views.ExploreView.as_view(), name='allStories'),

    path('story/<int:pk>/', views.StoryView.as_view(), name='story'),

    path('<int:pk>/comment/', views.AddCommentView.as_view(), name="addComment"),

    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('story/<int:pk>/edit/', views.EditStoryView.as_view(), name='editStory'),
    path('story/<int:pk>/delete/', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('delete-story-done/', views.DeleteStoryDoneView, name='deleteStory_done'),

]