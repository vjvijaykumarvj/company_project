from .models import Employee
from.forms import Emp_form
from django.shortcuts import render,redirect

def emp_dashboard(request):
    if request.method  == 'GET':
        employee_list = Employee.objects.all()
        emp_form = Emp_form()
        dict = {
            'emp_form': emp_form,
            'emp_list':employee_list
        }
        return render(request,'emp_find/dashboard.html',context=dict)
    elif request.method == 'POST':
        emp_form = Emp_form(request.POST)
        if emp_form.is_valid():
            emp_form.save()
        return redirect('/emp_dashboard/')

def emp_update(request,pk):
    if request.method=='GET':
        employee = Employee.objects.get(id=pk)
        emp_form = Emp_form(instance=employee)
        emp_list = Employee.objects.all()
        dict = {
            'emp_form' : emp_form,
            'emp_list' : emp_list,
            'is_update' : 'yes'
        }
        return render(request,'emp_find/dashboard.html',context=dict)
    elif request.method == 'POST':
        emp_db = Employee.objects.get(id=pk)
        emp_form = Emp_form(request.POST,instance=emp_db)
        if emp_form.is_valid():
            emp_form.save()
        return redirect('/emp_dashboard/')
def emp_delete(request,pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/emp_dashboard/')