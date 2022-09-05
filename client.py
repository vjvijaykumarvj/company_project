# #method over loading
# # class Patent:
# #     def name(self,x,y):
# #         print(x+y)
# #     def name(self,x,y,z):
# #         print(x+y+z)
# # obj = Patent()
# # obj.name(10,20,30)
#
#
# #methodoverriding
# # class parent1:
# #     def display(self):
# #         print('this is parent class called')
# # class child(parent1):
# #     def display(self):
# #         print('child method can be called')
# # obj1 = child()
# # obj1.display()
#
#
# students = [
#     {
#         "id": 101,
#         "name": "Kiran"
#     },
#     {
#         "id": 102,
#         "name": "Isha"
#     },
#     {
#         "id": 103,
#         "name": "John"
#     }
# ]
#
# grades = [
#     {
#         "student_id": 102,
#         "percentage": 73,
#         "qualification": "BE"
#     },
#     {
#         "student_id": 101,
#         "percentage": 65,
#         "qualification": "MCA"
#     },
#     {
#         "student_id": 103,
#         "percentage": 82,
#         "qualification": "Mtec"
#     }
# ]
#
# d = dict(students)
# e = dict(grades)
# z = dict(zip(students,grades))
# print(z)
# #
# # DROP TABLE EMPLOYEE;
# # DELETE * FROM EMPLOYEE WHERE COLOME_NAME;
# # DELETE * FROM EMPLOYEE WHERE SALARY = 100000
# # SELECT DISTINCT FROM EMPLOYEE SALARY;
#
#


# lst = [['Geeks', 1], ['For', 2], ['Geeks', 3]]
# l = dict(lst)
# print(l)


# def solution(A):
#     sum = 0
#     for i in A:
#         if i % 4 == 0:
#             sum= sum+i
#     return sum
# A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
# print(solution(A))

# class employee():
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def employee_called(self):
#         print('my name is: ',self.name)
#         print('my age is: ',self.age)
#         print('my salary is: ',self.salary)
# class student(employee):
#     def __init__(self,address,name,age,salary):
#         self.address = address
#         super().__init__(name,age,salary)
#     def student_called(self):
#         print('my address is: ',self.address)
#         super(student, self).employee_called()
# obj = student('bangaloe','vijay',23,50000)
# obj.student_called()
# # ob=employee('vijya',25,5000)
# # ob.employee_called()

# import json
# dict = {
#     'id':1,
#     'name':'vijay',
#     'salary' : 250000
# }
#
# x = json.dumps(dict)
# print(x)


# dictionary methods
# 1.get 2. keys 3.values 4.items 5.pop 6.popitem 7.setdefault 8.update 9. fromkeys 10.clear 11.Copy

# d = {1: 'vijay', 2: 'hamsa', 3: 'vamsi', 4: 'das', 5: 'bala'}
# d1 = {6: 'sasi', 7: 'pallavi', 8: 'manas', 9: 'kumar', 10: 'satvick'}

# print(dir(set))
# set methods
# 1.add 2.clear 3.copy 4.diffrent 5.diffrent_update 6.discard 7.intersection 9.intersection_udate 10.isdisjoint 11.issubset 12.issuperset
# 13.pop 14. remove 15.symentric_diffrence 16.symentric_diffrence_update 17.union 18.update

# s = {1, 2, 3, 4, 5}
# s1 = {10, 20, 5, 12}


# git config --global user.email email_name
# git config --global user.username
# git init this is current file name
# git status git status checking perpose used
# git clone 'urlpass here'
# git status
# git add <filename> or git add . working directory to staging area
# git commit -m 'add the vijay.py color add in google account' staging area to local repository
# git status
# git log this is used to check the all the previous all commits with log id
# git reset <filename> file delete purpose used
# git pull remote to local repositary
# git push local to remote repository
# git branch <branch name> branch create
# git checkout <branchname> go for perticular branch
# git branch -d <branchname> delete branch
# git diff <filename>


######################    MYSQL     #####################################
# create database <databasename>;
# drop database <databasename>;
# createtable <tablename> (
#       id     primarykey NOTNULL auto increment,
#       name   varchar(100) notnull,
#       age    int (20) notnull,
# );
# drop table <tablename>;
# alter table <tablename> add salary after age;
# altertable <tablename> modify name varchar(200);
# altertable <tablename> drop column age;
# alter table <tablename> rename <change tablename>;
# insert into <tablename>(id,name,age) values(1,'vijay',25),(2,'anitha',23);
# insert into <tablename> values(30,'pavani',24);
# select dicstinct name from <tablename>;
# select distinct age from <tablename>;
# select max(marks) from <tablename>;
# select min(marks) from <tablename>;
# select round(avg(marks)) from <tablename>;
# select sum(marks) from <tablename>;
# select * from <tablename>; totally data will came here
# select * from <tablename> where age between 10 and 30;
# select * from <tablename> orderby name ASC;
# select * from <tablename> orderby age DESC;
# update <table name> set name ='vijay' where age=23;
# delete from <tablename> where name='D';

# l = ['anitha','vnijay','sumathi','owl','pallavi','elephant']
# s = [1,43,23,64,473,5453,432,465,654,4375]


# l = 'vijaykumar123@gmail.com' # this is email valid
# l1 = 'vijay@13gmail.com' # this email not valid
# email = input('enter valid email')
#
# if email == l:
#     print('this is valid email id successfully login')
# elif email == None:
#     print('email is None')
# elif email == '':
#     print('email is None')
# elif email == 1234:
#     print('email is not valid because your enter totally numbers')
# else:
#     print('!!!!!!!!!!!  email error  !!!!!!!!!!!!!!')


# d = {1: 'malli', 2: 'sai', 3: 'bala', 4: 'das', 5: 'boss'}




#select max(salary) from employee



# SELECT SALARY FROM EMPLOYEE ORDERBY DESC LIMIT 2,1;

# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get('https://www.flipkart.com/oppo-k10-5g-ocean-blue-128-gb/p/itm28cf887931942?pid=MOBGGFFKHJ3HCSNR&lid=LSTMOBGGFFKHJ3HCSNRZB81YD&marketplace=FLIPKART&store=tyy%2F4io&srno=b_1_2&otracker=clp_banner_1_13.bannerX3.BANNER_mobile-phones-store_Z89JHXUYWOOX&fm=neo%2Fmerchandising&iid=e9389ca1-7635-4111-9a7e-0cb48bba82c9.MOBGGFFKHJ3HCSNR.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=wd96czvuww0000001661166138144')
# soup = BeautifulSoup(response.text,'html.parser')
# print(soup)


# input--------> [1,2,3,5,2,1,3,5]
# output-------> [1,1,2,2,3,3,5,5]


# def solution(A):
#     sum = 0
#     for i in A:
#         if i % 4 == 0:
#             sum= sum+i
#     return sum
# A = [-6, -91, 1011, -100, 84, -22, 0, 1, 473]
# print(solution(A))



# A = ['malli',7576,'susi',545,'sai','dharni',12,'Hamsa','Vijay',123,'pallavi','anitha']
# A = [10,12,43,56,54,78,90,67,94,91,100]



















