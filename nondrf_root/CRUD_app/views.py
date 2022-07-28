from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.core.serializers import serialize
import json
# Create your views here.
def Employee_cr(request):
        #crete the Employee object by using POST method
        if request . method == 'POST':
                #read the input data from client
                emp_json=request.body
                #convert the emp_json input data to dict formation
                try:
                    emp_dict=json.loads(emp_json)#json object to python convert [json <==loads==> python]
                except:
                    return HttpResponse(json.dumps({'messege':'Some errors occurs Please varify the Employee Record'}))
                #create tej database object
                employee = Employee(eno=emp_dict['eno'],name=emp_dict['name'],age=emp_dict['age'],salary=emp_dict['salary'],address=emp_dict['address'])
                #save the Employee object
                employee.save()
                #response from client
                resp_msg = {'message': 'Employee Creatd Successfully!!!!'}
                return HttpResponse(json.dumps(resp_msg),content_type='application/json')#convert the python to json object[python <==dumps==>json]
        elif request . method == 'GET':
                #GET The all Employee Details Using GET Function
                #Getting All Employee From Database
                emp_db = Employee.objects.all()
                # the Employee is the complex Or Query set objects so dividing the Employee By Using Serializing
                emp_json = serialize('json',emp_db)
                #convert The emp_json Object to dict formation by using loads
                temp_dict = json.loads(emp_json)
                final_employee=[]
                for emp in temp_dict:
                        obj = emp['fields']
                        obj['id'] = emp['pk']
                        final_employee.append(obj)
                #temp_dict will be return response of client by using dumps
                return HttpResponse(json.dumps(final_employee),content_type='application/json')

def Employee_rud(request,pk):
    if request . method  == 'GET':
        #now we want to perticular Employee Record from database
        try:
            emp_db = Employee.objects.get(id=pk)#(pk=01 )
        except:
            return HttpResponse(json.dumps({'messege':'Employee Record id={} Not Found Please mention Perticular Record'.format(pk)}),content_type='application/json')
        #this is complex object so we convert emp_db is manually convert dict format
        emp_dict={
                'id' : emp_db.id,
                'eno' : emp_db.eno,
                'name' : emp_db.name,
                'age' : emp_db.age,
                'salary' : emp_db.salary,
                'address' : emp_db.address,
        }
        return HttpResponse(json.dumps(emp_dict),content_type='application/json')
    elif request . method == 'PUT':#(PUT Is HTTP Method UPDATE)
        #read the input Update Employee Data from Client
        emp_input_json = request.body
        #convert the emp_input_json to dict form
        try:
            emp_dict = json.loads(emp_input_json)
        except:
            return HttpResponse(json.dumps({'msg':'Please mention details perfectly'}),content_type='application/json')
        #gow we update the perticular Employee Record
        try:
            employee = Employee.objects.get(id=pk)
        except:
            return HttpResponse(json.dumps({'messege': 'id={} not matching'.format(pk)}),
                                content_type='application/json')

        #create the Employee model object form (instance)
        employee = EmployeeForm(emp_dict,instance=employee)
        if employee.is_valid():
            employee.save()
        return HttpResponse(json.dumps({'messege' : 'Update Employee Successfully'}),content_type='application/json')

    elif request . method == 'DELETE':
        #get the Employee Record From Database
        try:
            emp_db = Employee.objects.get(id=pk)
        except:
            return HttpResponse(json.dumps({'msg':'Please mention perticular id={}'.format(pk)}),content_type='application/json')
        emp_db.delete()
        return HttpResponse(json.dumps({'messege' : 'DELETE The Employee Record'}),content_type='aplication/json')

from django.views.generic import View
class Employee_CR(View):
    def post(self,request,*args,**kwargs):
        #read the Employee Record From Client
        emp_json = request.body
        #convert the dict format
        emp_dict = json.loads(emp_json)
        emp_form = EmployeeForm(emp_dict)
        if emp_form.is_valid():
            emp_form.save()
        return HttpResponse(json.dumps({'messege':'Create the Employee Successfully'}),content_type='application/json')
    def get(self,request,*args,**kwargs):
        # GET The all Employee Details Using GET Function
        # Getting All Employee From Database
        emp_db = Employee.objects.all()
        # the Employee is the complex Or Query set objects so dividing the Employee By Using Serializing
        emp_json = serialize('json', emp_db)
        # convert The emp_json Object to dict formation by using loads
        temp_dict = json.loads(emp_json)
        final_employee = []
        for emp in temp_dict:
            obj = emp['fields']
            obj['id'] = emp['pk']
            final_employee.append(obj)
        # temp_dict will be return response of client by using dumps
        return HttpResponse(json.dumps(final_employee), content_type='application/json')
class Employee_RUD(View):
    def get(self,request,pk,*args,**kwargs):
        try:
            emp_db = Employee.objects.get(id=pk)#(pk=01 )
        except:
            return HttpResponse(json.dumps({'messege':'Employee Record id={} Not Found Please mention Perticular Record'.format(pk)}),content_type='application/json')
        #this is complex object so we convert emp_db is manually convert dict format
        emp_dict={
                'id' : emp_db.id,
                'eno' : emp_db.eno,
                'name' : emp_db.name,
                'age' : emp_db.age,
                'salary' : emp_db.salary,
                'address' : emp_db.address,
        }
        return HttpResponse(json.dumps(emp_dict),content_type='application/json')
    def put(self,request,pk,*args,**kwargs):
        # read the input Update Employee Data from Client
        emp_input_json = request.body
        # convert the emp_input_json to dict form
        try:
            emp_dict = json.loads(emp_input_json)
        except:
            return HttpResponse(json.dumps({'msg': 'Please mention details perfectly'}),
                                content_type='application/json')
        # gow we update the perticular Employee Record
        try:
            employee = Employee.objects.get(id=pk)
        except:
            return HttpResponse(json.dumps({'messege': 'id={} not matching'.format(pk)}),
                                content_type='application/json')

        # create the Employee model object form (instance)
        employee = EmployeeForm(emp_dict, instance=employee)
        if employee.is_valid():
            employee.save()
        return HttpResponse(json.dumps({'messege': 'Update Employee Successfully'}), content_type='application/json')
    def delete(self,request,pk,*args,**kwargs):
        # get the Employee Record From Database
        try:
            emp_db = Employee.objects.get(id=pk)
        except:
            return HttpResponse(json.dumps({'msg': 'Please mention perticular id={}'.format(pk)}),
                                content_type='application/json')
        emp_db.delete()
        return HttpResponse(json.dumps({'messege': 'DELETE The Employee Record'}), content_type='aplication/json')