from rest_framework import serializers
from.models import Rooms

class roomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'