from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def load_employee(request):
    employee_load=Employee.objects.all()
    emp_dict={
        'employee_load'  :   employee_load
    }
    return render(request,'company_app/load_employee.html',context=emp_dict)

def employee_create(request):
    if request.method =='GET':
       return render(request,'company_app/employee_create.html')
    elif request.method=='POST':
        eno=request.POST.get('emp_number')
        name=request.POST.get('name')
        age=request.POST.get('age')
        salary=request.POST.get('salary')
        address=request.POST.get('address')
    employee=Employee(eno=eno,name=name,age=age,salary=salary,address=address)
    employee.save()
    return redirect('/employee/')

def emp_info(request,pk):
    employee=Employee.objects.get(id=pk)
    emp_dict={
        'employee'  :  employee
    }
    return render(request,'company_app/emp_id.html',context=emp_dict)

def emp_delete(request,pk):
    employee=Employee.objects.get(id=pk)
    employee.delete()
    return redirect('/employee/')

def emp_update(request,pk):
    if request.method=='GET':
       employee=Employee.objects.get(id=pk)
       employee_dict={
           'employee'   :   employee
       }
       return render(request,'company_app/employee_create.html',context=employee_dict)
    elif request.method=='POST':
        employee = Employee.objects.get(id=pk)
        eno = request.POST.get('emp_number')
        name = request.POST.get('name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        address = request.POST.get('address')
        #employee = Employee(eno=eno, name=name, age=age, salary=salary, address=address)
        employee.eno=eno
        employee.name=name
        employee.age=age
        employee.salary=salary
        employee.address=address
        employee.save()
    return redirect('/employee/')


from django.http import HttpResponse
from django.views.generic import View,ListView

class TestCBV(View):
    def get(self,request):
        msg='@@@@ THIS IS GET PAGE @@@@'
        data={
            'msg'  : msg
        }
        return render(request,'company_app/cbv/test.html',context=data)
        #return HttpResponse(msg)
    def post(self,request):
        msg='This is POST method called'
        return HttpResponse(msg)
    def update(self,request):
        msg='this is UPDATE method'
        return HttpResponse(msg)
    def delete(self,request):
        msg='this is delete method'
        return HttpResponse(msg)

class ListEmployeeCBV(ListView):
    Model=Employee
    context_object_name='employee_load'
    template_name='company_app/cbv/load_employee.html'











