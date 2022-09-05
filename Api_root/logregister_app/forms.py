from django import forms
from.models import model_emp


class Emp_form(forms.ModelForm):
    class Meta:
        model = model_emp
        fields = '__all__'
