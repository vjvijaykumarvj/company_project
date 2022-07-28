from django import forms
from .models import Employee


class EmployeeForms(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        widgets={
            'eno' : forms.TextInput(attrs={'class':'form-control'}),
            'name' :forms.TextInput(attrs={'class':'form-control'}),
            'age' :forms.TextInput(attrs={'class':'form-control'}),
            'salary' :forms.TextInput(attrs={'class':'form-control'}),
            'address' :forms.TextInput(attrs={'class':'form-control'}),
        }
