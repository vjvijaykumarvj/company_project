from django.shortcuts import render,redirect
from .forms import EmployeeForms
from .models import Employee
# Create your views here.

def employee_dashboard(request):
    if request.method=='GET':
        employee_form=EmployeeForms()
        emp_list=Employee.objects.all()
        emp_dict={
            'employee_form' : employee_form,
            'emp_list'  :  emp_list
        }
        return render(request,'modelforms_app/create_employee.html',context=emp_dict)
    # read the all request data from
    elif request.method=='POST':
        employee_form=EmployeeForms(request.POST)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('employee_form/employee_dashboard/')

def Update_employee(request,pk):
    if request.method=='GET':
        employee=Employee.objects.get(id=pk)
        employee_form=EmployeeForms(instance=employee)
        emp_list=Employee.objects.all()
        emp_dict={
            'employee_form':employee_form,
            'emp_list':emp_list
        }
        return render(request, 'modelforms_app/create_employee.html', context=emp_dict)
    elif request.method=='POST':
        emp_list=Employee.objects.get(id=pk)
        employee_form = EmployeeForms(request.POST,instance=emp_list)
        if employee_form.is_valid():
            employee_form.save()
            return redirect('employee_form/employee_dashboard/')




