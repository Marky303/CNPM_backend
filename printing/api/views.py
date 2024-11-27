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
def ViewParameters(request):
    try:
        error = []

        # Check if there is an error
        if error:
            raise Exception()

        # Response
        return ResponseSuccessful()
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
