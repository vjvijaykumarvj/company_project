from django.shortcuts import render
from datetime import datetime


def home(request):
    return render(request,'home.html')
def contactus(request):
    return render(request,'contactus.html')
def aboutus(request):
    return render(request,'aboutus.html')
def dtl(request):
    Firstname = 'Vijay'
    Lastname  = 'Kumar'
    Age   =   20
    Address = 'Bangalore'
    fruitsLists=['bananna','apple','sapoto']
    items={
        1001 : 'python',
        1002 : 'java',
        1003 : 'bigdata'
    }

    class employee:
        def __init__(self,name,age,salary):
            self.name=name
            self.age=age
            self.salary=salary
    emp=employee('anitha',23,34000)

    datenows = datetime.now()
    numdict={
        400:'vijay',
        401:'anitha',
        403:'eswaramma',
        404:'subramanyam'
    }
    class family:
        def __init__(self,father,mother,son,daughter):
            self.father=father
            self.mother=mother
            self.son=son
            self.daughter=daughter
    ethis=family('subramanyam','eswaramma','vijay','anitha')


    parts={
        'firstname' :  Firstname,
        'lastname'  :  Lastname,
        'age'       :  Age,
        'address'   :  Address,
        'lists'     :  fruitsLists,
        'Items'     :  items,
        'Emp'       :  emp,
        'datenow'    :   datenows,
        'numdict'   :  numdict,
        'Ethis'     : ethis
    }

    return render(request,'dtl.html',context=parts)