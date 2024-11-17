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
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ViewPrinter(request):
    error=[]
    VerifySPSOinfo(request,error)
    if error:
            raise Exception()
    try: 
        printer_list =ViewPrinter(request) 
        printer=to_json(printer_list)
        return Response({"printers": printer}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def detelePrinter(request,id):
    error=[]
    VerifySPSOinfo(request,error)
    if error:
            raise Exception()
    try:
        deletePrinter(id) 
        return Response({"success": True}, status=200)
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=400)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addNewPrinter(request):
    error=[]
    VerifySPSOinfo(request,error)
    if error:
            raise Exception()
    try:
        data = json.loads(request.body)
        name = data.get('name')
        serial_number = data.get('serial_number')
        connection_key = data.get('connection_key')
        location = data.get('location')
        building = data.get('building')
        status = data.get('status', 'AVAILABLE')
        if not all([name, serial_number, connection_key, location, building]):
            return Response({"success": False, "error": "Missing required fields"}, status=400)
        createPrinter(name,serial_number,connection_key,location,building,status)
        return Response({"success": True },status=201)
    except Exception as e:
        return Response({"success": False, "error": str(e)}, status=400)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePrinter(request,id):
    error=[]
    VerifySPSOinfo(request,error)
    if error:
            raise Exception()
    try:
        data = json.loads(request.body)
        name = data.get('name')
        serial_number = data.get('serial_number')
        connection_key = data.get('connection_key')
        location = data.get('location')
        building = data.get('building')
        status = data.get('status', 'AVAILABLE')
        if not all([name, serial_number, connection_key, location, building]):
            return Response({"success": False, "error": "Missing required fields"}, status=400)
        printer = updateprinter(id, name, serial_number, connection_key, location, building, status)
        printer_data=to_json([printer])
        return Response({"success": True, "printer": printer_data}, status=200)
    except Exception as e:
            return Response({"success": False, "error": str(e)}, status=400)
