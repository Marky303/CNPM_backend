from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Printing related urls
    path('printdocument/', views.PrintDocument),
    path('viewPrinter/',views.ViewPrinter),
    path('deletePrinter/<int:id>/',views.detelePrinter),
    path('addNewPrinter',views.addNewPrinter),
    path('updatePrinter/<int:id>',views.updatePrinter),
]