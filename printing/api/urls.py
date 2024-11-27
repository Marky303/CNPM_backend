from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Printing related urls
    path('printdocument/', views.PrintDocument),
    path('viewanalysis/', views.ViewAnalysis),
    path('adjustparameters/', views.AdjustParameters),
    path('viewparameters/', views.ViewParameters),
]
