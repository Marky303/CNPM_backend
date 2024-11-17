import ast
from datetime import datetime
import random
import string
from decimal import Decimal

# Import models
from printing.models import *

def CreateNewPrintHistory(request):
    pass
def ViewPrinter(requuest):
    try:
        printers = Printer.objects.all()
        return {"success": True, "printers": printers}
    except Exception as e:
        return {"success": False, "error": str(e)}
def deletePrinter(printer_id):
    try:
        printer = Printer.objects.get(id=printer_id)
        printer.delete()
    except Printer.DoesNotExist:
        raise ValueError(f"Printer with id {printer_id} not found.")
    
def createPrinter(name, serial_number, connection_key, location, building, status):
    printer = Printer.objects.create(
        Name=name,
        SerialNumber=serial_number,
        ConnectionKey=connection_key,
        Location=location,
        Building=building,
        Status=status
    )
def updateprinter(printer_id, name=None, serial_number=None, connection_key=None, location=None, building=None, status=None):
    try:
        printer = Printer.objects.get(id=printer_id)
        if name:
            printer.Name = name
        if serial_number:
            printer.SerialNumber = serial_number
        if connection_key:
            printer.ConnectionKey = connection_key
        if location:
            printer.Location = location
        if building:
            printer.Building = building
        if status:
            printer.Status = status
        printer.save()
        return printer

    except Printer.DoesNotExist:
        raise ValueError(f"Printer with id {printer_id} not found.")
