from django.urls import path

# Importing related views
from . import views

# Setting up urls patterns
urlpatterns = [
    # Setting
    path('getsettings/'         , views.GetSettings),
    path('changesettings/'      , views.ChangeSettings),
    
    # History related urls
    path('history/'             , views.CheckHistory),
    
    # Token related urls
    path('buytoken/'            , views.BuyToken),
    
    # Printing related urls
    path('getactiveprinters/'   , views.GetActivePrinters),
    path('printdocument/'       , views.PrintDocument),
    
    # Printer management
    path('getallprinters/'      , views.GetAllPrinters),
    path('createnewprinter/'    , views.CreateNewPrinter),
    path('editprinter/'         , views.EditPrinter),
    path('deleteprinter/'       , views.DeletePrinter),
    path('toggleprinter/'       , views.TogglePrinter),
]