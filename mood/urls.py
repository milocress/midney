from django.urls import path
from mood import views

urlpatterns = [
    path('thinkers/', views.thinker_list),
    path('moods/<int:thinker>/<int:mood>', views.mood_append),
]
