from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Employee
