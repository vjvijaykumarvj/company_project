from django.shortcuts import render, redirect
from.models import model_emp
from.forms import Emp_form
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def Register(request):
    if request.method == 'GET':
        return render(request,'logregister_app/register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # validation parts starthere
        if username == username or first_name == first_name or last_name==last_name or email==email or password==password or cpassword==cpassword:
            messages.error(request,'mandatary fields are misiing')
            return render(request, 'logregister_app/register.html')
        # password and cpassword not match give the error
        if password != cpassword:
            messages.error(request,'password andcpassword not match')
            return render(request, 'logregister_app/register.html')
        # username already exists give the error
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exists')
            return render(request, 'logregister_app/register.html')
        elif User.objects.filter(email=email).exists():
            messages.error(request,'email already exists')
            return render(request, 'logregister_app/register.html')
        # if there is no error go for the login page
        else:
            user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,cpassword=cpassword)
            return redirect('/user_login/')
def user_login(request):
    if request.method=='GET':
        return render(request,'logregister_app/userlogin.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/profile/')
        else:
            messages.error(request,'username and password invalid')
            return redirect('/user_login/')
def profile(request):
    return redirect(request,'logregister_app/register.html')
def user_logout(request):
    logout(request)
    return redirect('/user_login/')

