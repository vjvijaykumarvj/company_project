from django.shortcuts import render, redirect
from.models import Employee
from.forms import Emp_form

def emp_load(request):
    if request.method =='GET':
        emp_form = Employee.objects.all()
        emp_dict = {
            'emp_form_list' : emp_form
        }
        return render(request,'forms_app/emp_load.html',context=emp_dict)

def emp_create(request):
    if request.method == 'GET':
        return render(request,'forms_app/emp_create.html')
    elif request.method == 'POST':
        emp_form = Emp_form(request.POST)
        if emp_form.is_valid():
            emp_form.save()
        return redirect('/emp_load/')

def emp_id(request,pk):
    employee = Employee.objects.get(id=pk)
    dict = {
        'employee':employee
    }
    return render(request,'forms_app/emp_id.html',context=dict)

def emp_update(request,pk):
    pass
def emp_delete(request,pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    return redirect('/emp_load/')