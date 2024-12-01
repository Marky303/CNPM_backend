import json
from datetime import datetime
import random
import string
from decimal import Decimal
import math

# Import models
from printing.models import *

def CreateNewPrintHistory(request):
    pass

# Print management related___________________________________________
def GetAllPrintersCRUD():
    return Printer.objects.all()

def CreateNewPrinterCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Create new printer from body
    printer = Printer(Name          = info['Name'],
                      SerialNumber  = info['SerialNumber'],
                      Brand         = info['Brand'],
                      Location      = info['Location'],
                      Model         = info['Model'],
                      Status        = 'available')
    
    # Save new printer to database
    printer.save()
    
def EditPrinterCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get printer
    printer = Printer.objects.get(id=info['id'])
    
    # Edit printer
    printer.Name            = info['Name']
    printer.SerialNumber    = info['SerialNumber']
    printer.Brand           = info['Brand']
    printer.Location        = info['Location']
    printer.Model           = info['Model']
    
    # Save printer to database
    printer.save()
    
def DeletePrinterCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get printer
    printer = Printer.objects.get(id=info['id'])
    
    # Delete printer from database
    printer.delete()