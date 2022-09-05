from django.shortcuts import render, redirect
from.models import Book,Library
from.forms import Library_form,Book_form
# Create your views here.

def home(request):
    return render(request,'home.html')

def adminhome(request):
    return render(request, 'adminhome.html')

def new_book(request):
    if request.method == 'GET':
        return render(request,'new_app/book.html')
    elif request.method == 'POST':
        user = Library_form(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/home/')
def new_lobrary(request):
    if request.method == 'GET':
        return render(request,'new_app/library.html')
    elif request.method == 'POST':
        user = Library_form(request.POST)
        if user.is_valid():
            user.save()
        return redirect('/adminhome/')


