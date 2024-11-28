from printing.models import History
from rest_framework.serializers import ModelSerializer      

class HistorySerializer(ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'
