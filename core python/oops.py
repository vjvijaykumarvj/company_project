# class Test:
#     '''document class test '''
#     a=10
#     def __init__(self):
#         self.b=20
#         self.c=30
#         Test.x=100
#     def m1(self):
#         Test.y=200
#
#     @classmethod
#     def m2(cls):
#         cls.z=300
#         Test.z1=400
#     @staticmethod
#     def m3():
#         Test.z2=500
# obj = Test()
# # obj.m1()
# # obj.m2()
# # obj.m3()
# Test.m3()
# print(Test.__dict__)
#

class Student:
    org_name='TCS RECRUITMENT'
#    print(org_name)

    def __init__(self,org_name,eno,name,age,salary,address):
        self.eno=eno
        self.name=name
        self.age=age
        self.salary=salary
        self.address=address
    def Details(self):
        print('my Employee number :{}  '.format(self.eno))
        print('my Employee name :{}  '.format(self.name))
        print('my Employee age :{}  '.format(self.age))
        print('my Employee salary :{}  '.format(self.salary))
        print('my Employee address :{}  '.format(self.address))
obj = Student('Tcs consultancy',1001,'vijay',23,2345,'vgr')
#obj2 = Student(1002,'kumar',22,23452,'ban')
obj.Details()
print(obj.org_name)
print('#######################################################################')
#obj2.Details()
#print(Student.__dict__)















