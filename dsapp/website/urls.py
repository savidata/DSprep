from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('flashcards', views.flashcards, name="flash"),
    path('questions', views.questions, name="questions"),
    path('interview', views.interview, name="interview"),

]