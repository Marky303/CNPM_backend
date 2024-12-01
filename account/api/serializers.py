from djoser.serializers import UserCreateSerializer
from rest_framework.serializers import ModelSerializer

# Get custom user model
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password') 
                
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
                
                
                
                
                
                
                
# EXAMPLE SERIALIZER FOR TESTING
# Note model for testing
from account.models import Note
from rest_framework.serializers import ModelSerializer        

# Note serializer
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'