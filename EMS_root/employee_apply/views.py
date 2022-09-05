from django.shortcuts import render, redirect
from .models import Employee
from.forms import Employee_form

def Employee_load(request):
    if request.method == 'GET':
        form_list = Employee.objects.all()
        emp_dict = {
            'form_list' : form_list
        }
        return render(request,'employee_apply/employee_load.html',context=emp_dict)
def emp_create(request):
    if request.method =='GET':
        return render(request,'employee_apply/create_employee.html')
    elif request.method=='POST':
        emp_form = Employee_form(request.POST)
        if emp_form.is_valid():
            emp_form.save()
        return redirect('/emp_Apply/')
def emp_id(request,pk):
    employee = Employee.objects.get(id=pk)
    emp_dict = {
        'employee':employee
    }
    return render(request,'employee_apply/employee_id.html',context=emp_dict)

def emp_update(request,pk):
    if request.method == 'GET':
        em_db = Employee.objects.get(id=pk)
        # emp_form = Employee_form(instance=em_db)
        emp_dict = {
            'employee':em_db,
            # 'emp_form':emp_form
        }
        return render(request,'employee_apply/create_employee.html',context=emp_dict)
    elif request.method == 'POST':
        employee  =Employee.objects.get(id=pk)
        emp_form = Employee_form(request.POST,instance=employee)
        if emp_form.is_valid():
            emp_form.save()
        return redirect('/emp_Apply/')
def emp_delete(request,pk):
    emp_db =Employee.objects.get(id=pk)
    emp_db.delete()
    return redirect('/emp_Apply/')