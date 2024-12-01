import json
from datetime import datetime
import random
import string
from decimal import Decimal
import math
import os
from django.db.models import Q

# Import models
from printing.models import *
from account.models import *

# Settings related___________________________________________________
def GetSettingsCRUD():
    setting = Setting.objects.get(id=1)
    template = {
        "Token": setting.Token,
        "AllowedFiles": setting.AllowedFiles,
        "Time": setting.Time,
    }
    return template

def ChangeSettingsCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get the setting entry
    setting = Setting.objects.get(id=1)
    
    # Change setting
    setting.AllowedFiles = info['AllowedFiles']
    setting.Token = info['Token']
    setting.Time = info['Time']
    setting.save()

# History related____________________________________________________
def CheckHistoryCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get history for spso
    if request.user.is_SPSO:
        data = History.objects.all()
    # Get history for user
    else:
        data = History.objects.filter(User=request.user)
        
    # Apply printer filter
    try:
        printer = Printer.objects.get(id=info['PrinterID'])
        data = data.filter(Printer=printer)
    except Printer.DoesNotExist:
        pass
        
    # Apply date filter
    fromdate = info['From']
    todate = info['To']
    
    # Build query filters
    query = Q()
    if fromdate:
        query &= Q(Date__gte=datetime.strptime(fromdate, "%Y-%m-%d"))
    if todate:
        query &= Q(Date__lte=datetime.strptime(todate, "%Y-%m-%d"))

    # Apply the filters if any condition is added
    if query:
        data = data.filter(query)
        
    return data



# Token related______________________________________________________
def BuyTokenCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get number of token 
    token = int(info['token'])
    
    # Give user tokens
    user = request.user
    user.token += token
    user.save()
    
    return token
    
    

# Print related______________________________________________________
def GetActivePrintersCRUD():
    return Printer.objects.filter(Status='Available')

def CreateNewPrintHistory(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get the printer
    printer = Printer.objects.get(id=info['PrinterID'])
    
    # Get cost
    pageMultiplier = 1
    if info['Size'] == 'A3':
        pageMultiplier = 2
    if info['Size'] == 'A3':
        pageMultiplier = 4
    cost = pageMultiplier * int(info['Pages']) * int(info['Copies'])
    
    # Get the file type
    fileType = os.path.splitext(info['FileName'])[1][1:]
    print(fileType)
    
    # Create new print history
    history = History(Date              = datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                      Location          = printer.Location,
                      Direction         = info['Direction'],
                      FileName          = info['FileName'],
                      Pages             = info['Pages'],
                      Copies            = info['Copies'],
                      Cost              = cost,
                      Size              = info['Size'],
                      FileType          = fileType,
                      Printer           = printer,
                      User              = request.user)
    
    history.save()

    # Deduct from token
    user = request.user
    user.token = user.token - cost
    user.save()


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
                      Status        = 'Available')
    
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
    
def TogglePrinterCRUD(request):
    # Converting request.body to dictionary type
    dict = request.body.decode("UTF-8")
    info = json.loads(dict)
    
    # Get printer
    printer = Printer.objects.get(id=info['id'])
    
    # Toggle
    if printer.Status == 'Available':
        printer.Status = 'Maintenance'
    else:
        printer.Status = 'Available'
        
    # Save to database
    printer.save()