from rest_framework.serializers import ModelSerializer       
from printing.models import *
import json

# General JSOn serializer (from dictionary)
def SerializeResponse(result):
    serializedResult = json_string = json.dumps(result)    
    return result

# Printer serializer
class PrinterSerializer(ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'
        
# History serializer
class CustomerPrinterSerializer(ModelSerializer):
    class Meta:
        model = Printer
        fields = ['Name']

class HistorySerializer(ModelSerializer):
    Printer = CustomerPrinterSerializer()
    
    class Meta:
        model = History
        fields = '__all__'