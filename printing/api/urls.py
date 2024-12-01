from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Printing related urls
    path('printdocument/', views.PrintDocument),
    
    # Printer management
    path('getallprinters/'      , views.GetAllPrinters),
    path('createnewprinter/'    , views.CreateNewPrinter),
    path('editprinter/'         , views.EditPrinter),
    path('deleteprinter/'       , views.DeletePrinter),
]