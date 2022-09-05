from rest_framework import serializers
from.models import Employee_view


class Emp_serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_view
        fields = '__all__'
