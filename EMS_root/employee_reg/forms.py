from.models import Contact,Employee_model
from django import forms


class Contact_form(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class Employee_form(forms.ModelForm):
    class Meta:
        model = Employee_model
        fields = '__all__'