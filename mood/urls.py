from django.urls import path
from mood import views

urlpatterns = [
    path('thinkers/', views.thinker_list),
    path('moods/', views.mood_append),
]
