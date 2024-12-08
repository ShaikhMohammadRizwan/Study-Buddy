from rest_framework import serializers  # Correct import for serializers
from base.models import Room

class RoomSerializer(serializers.ModelSerializer):  # Corrected the class name to ModelSerializer
    class Meta:
        model = Room
        fields = '__all__'
