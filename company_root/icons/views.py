from django.shortcuts import render
from . models import Student
# Create your views here.


def icons(request):
    return render(request,'icons/icon.html')
def student(request):
    if request . method == 'GET':
        return render(request,'icons/studentreg.html')
    elif request . method == 'POST':
        Firstname = request . POST . get('firstname')
        Lastname = request . POST . get('lastname')
        Gender = request . POST . get('gender')
        Age = request . POST . get('age')
        Contactnumber = request . POST . get('contactnumber')
        Emailid = request . POST . get('emailid')
        Address = request . POST . get('address')
        City = request . POST . get('city')
        State = request . POST . get('state')
        Python = request . POST . get('python')
        Datascience = request . POST . get('datascience')
        Bigdata = request . POST . get('bigdata')
        Username = request . POST . get('username')
        Password = request . POST . get('password')

    student = Student(firstname=Firstname,lastname=Lastname,gender=Gender,age=Age,contactnumber=Contactnumber,
                      emailid=Emailid,address=Address,city=City,state=State,python=Python,datascience=Datascience,
                      bigdata=Bigdata,username=Username,password=Password)
    student.save()

    dict={
        'firstname'    :  Firstname,
        'lastname'     :   Lastname,
        'gender'       :   Gender,
        'age'          :     Age,
        'contactnumber':    Contactnumber,
        'emailid'      :  Emailid,
        'address'      :     Address,
        'city'         :     City,
        'state'        :   State,
        'python'       :    Python,
        'datascience'  :     Datascience,
        'bigdata'      :    Bigdata,
        'username'     :    Username,
        'password'     :    Password
        }
    return render(request,'icons/studentdetails.html',context=dict)