from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Import printing related functions, classes
from printing.api.Functions.verify import *
from printing.api.Functions.CRUD import *
from printing.api.Functions.response import *
from printing.api.Functions.printerAPI import *
from printing.api.serializers import *

# Get dashboard_____________________________________________________
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetDashboard(request):
    try:
        error = []
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all printer from database
        data = GetDashboardCRUD()
        
        serializedData = SerializeResponse(data)
        
        # Response
        return ResponseObject(serializedData)
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)

# Settings related__________________________________________________
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetSettings(request):
    try:
        error = []
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all printer from database
        data = GetSettingsCRUD()
        
        serializedData = SerializeResponse(data)
        
        # Response
        return ResponseObject(serializedData)
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ChangeSettings(request):
    try:
        error = []
        
        # Error check...
        VerifySettings(request, error)
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all printer from database
        ChangeSettingsCRUD(request)
        
        # Response
        return ResponseSuccessful("Thay đổi cài đặt thành công")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    

# History related________________________________________________
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CheckHistory(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all printer from database
        data = CheckHistoryCRUD(request)
        
        # Serialize the thingy
        serializedData = HistorySerializer(data, many=True)
        
        # Response
        return ResponseObject(serializedData.data)
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    

# Token related__________________________________________________
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BuyToken(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all printer from database
        tokenBought = BuyTokenCRUD(request)
        
        # Response
        return ResponseSuccessful("Mua thành công " + str(tokenBought) + " tokens")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)



# Print document related_________________________________________
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetActivePrinters(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Get all printer from database
        data = GetActivePrintersCRUD()
        
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
        return ResponseSuccessful("Tài liệu đã được in!")
        
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
        return ResponseSuccessful("Đã thêm máy in mới")
        
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
        return ResponseSuccessful("Đã chỉnh sửa thông tin máy in")
        
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
        return ResponseSuccessful("Đã xóa máy in")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def TogglePrinter(request):
    try:
        error = []
        
        # Error check...
        
        # Check if there is an error
        if error:
            raise Exception()
        
        # Delete printer from database
        TogglePrinterCRUD(request)
        
        # Response
        return ResponseSuccessful("Toggled printer")
        
    except Exception as e:
        # Response a error code and error content
        if str(e):
            error.append(str(e))
        return ResponseError(error)
    
    