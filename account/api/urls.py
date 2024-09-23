from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Note example url
    path('getNotes/', views.getNotes)
    
]