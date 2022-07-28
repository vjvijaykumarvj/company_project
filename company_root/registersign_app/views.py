from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def sign_app(request):
    if request.method=='GET':
       return render(request,'registersign_app/sign.html')
    elif request.method=='POST':
        #reading the data from the request objects:
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        # 1. Validations fields are required are checking:
        if username=='' or email=='' or password=='' or cpassword=='' :
            messages.error(request,'Mandatary fields are missing')
            return render(request,'registersign_app/sign.html')
        # 2. password are matching are conform::::
        if password !=cpassword:
            messages.error(request,'password and conform password are not matching')
            return render(request,'registersign_app/sign.html')
        # 3. username already exists are not checking:::
        if User.objects.filter(username=username):
            messages.error(request,'Username already exists !!!')
            return render(request,'registersign_app/sign.html')
        # 3.1 Emailid are correct or already exists are checking or not:::
        elif User.objects.filter(email=email).exists():
            messages.error(request,'Emailid already exixts !!!')
            return render(request,'registersign_app/sign.html')
        # 3.2 All are ok To Store dat Into Data Base:::
        else:
            User.objects.create_user(username=username,first_name=first_name,last_name=last_name,
                                     email=email,password=password)
            return redirect('/login_app/login/')



def login_details(request):
    if request.method=='GET':
      return render(request,'registersign_app/login.html')
    elif request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)

        if User is not None:
            login(request, user)
            return redirect('/login_app/profilepage')
        else:
            messages.error(request,'Username/Password already exists')
            return redirect('/login_app/login/')

def profilepage(request):
    return render(request,'registersign_app/profilepage.html')


def logout_details(request):
    logout(request)
    return redirect('/login_app/login')





