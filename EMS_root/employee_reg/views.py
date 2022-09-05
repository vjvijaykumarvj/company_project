from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Contact,Employee_model
from.forms import Contact_form,Employee_form
from django.contrib import messages

def Home(request):
    return render(request,'employee_reg/home.html')
def aboutus(request):
    return render(request,'employee_reg/aboutus.html')
def contactus(request):
    if request.method == 'GET':
        form_data = Contact_form
        dict = {
            'form_data':form_data
        }
        return render(request,'employee_reg/contactus.html',context=dict)
    elif request.method == 'POST':
        form = Contact_form(request.POST)
        try:
            if form.is_valid():
                form.save()
            return redirect('/contactus/')
        except:
            msg = {'please write some msg'}
            return render(request,'employee_reg/contactus.html',context=msg)

def employee_register(request):
    if request.method =='GET':
        reg_form = Employee_form
        dict = {
            'reg_form':reg_form
        }
        return render(request,'employee_reg/employee_register.html',context=dict)
    elif request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        city =request.POST['city']
        email =request.POST['email']
        address =request.POST['address']
        password = request.POST['password']
        c_password =request.POST['c_password']
        username = request.POST['username']

        if username =='' or email == '' or password == ''or c_password =='' :
            messages.error(request ,'mandatary fields are missing')
            return render(request,'employee_reg/employee_register.html')
        if password !=c_password:
            messages.error(request,'password and conform password not matching')
            return render(request,'employee_reg/employee_register.html')
        if User.objects.filter(username = username):
            messages.error(request,'username is already exists')
            return render(request,'employee_reg/employee_register.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'email is alredy exists')
            return render(request,'employee_reg/employee_register.html')
        else:
            user = User.objects.create_user(username=username,password=password,
                   email=email)
            return redirect('/employee_login/')

def employee_login(request):
    if request.method == 'GET':
        return render(request,'employee_reg/employee_login.html')
    elif request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        login(request,user)
        return redirect('/')
    else:
        messages.error(request,'invalid credential')
        return render(request,'employee_reg/employee_login.html')
def employee_logout(request):
    logout(request)
    return redirect('/employee_login/')





