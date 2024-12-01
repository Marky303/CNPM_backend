from rest_framework.serializers import ModelSerializer       
from printing.models import *

# General JSOn serializer (from dictionary)

# Printer serializer
class PrinterSerializer(ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'