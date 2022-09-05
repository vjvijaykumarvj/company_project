from django import forms
from.models import Book,Library


class Book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class Library_form(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'