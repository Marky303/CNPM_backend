from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import printing related functions, classes
from printing.api.Functions.verify import *
from printing.api.Functions.CRUD import *
from printing.api.Functions.response import *
from printing.api.Functions.printerAPI import *
from printing.api.serializers import *

# Print document view
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PrintDocument(request):
    try:
        error = []
        
        # Check if print info
        VerifyPrintInfo(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Schedule print document
        Print(request)
        
        # Add new print info into database
        CreateNewPrintHistory(request)
        
        # Response
        return ResponseSuccessful("Document is being printed!")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    
# Printer management______________________________________________
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetAllPrinters(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all printer from database
        data = GetAllPrintersCRUD()
        
        # Serialize the thingy
        serializedData = PrinterSerializer(data, many=True)
        
        # Response
        return ResponseObject(serializedData.data)
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateNewPrinter(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Create new printer in database
        data = CreateNewPrinterCRUD(request)
        
        # Response
        return ResponseSuccessful("Created new printer")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def EditPrinter(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Edit printer in database
        EditPrinterCRUD(request)
        
        # Response
        return ResponseSuccessful("Edited printer")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def DeletePrinter(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Delete printer from database
        DeletePrinterCRUD(request)
        
        # Response
        return ResponseSuccessful("Deleted printer")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)