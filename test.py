# l = [89, 45, 67, 23]
#o/p = [23,45,67,89]
# def swap(l):
#     l[0],l[-1] = l[-1],l[0]
#     print(l)
# swap([89, 45, 67, 23])
# s = 'helloworld'
# a = (filter(lambda x:x[0].lower() in 'aeiou',s))

# z = {i:s.count(i) for i in s}
# print(z)
# z =list(filter(lambda x:x[0].lower() in 'aeiou',s))
# print(z)

# a = [10,1,100,5,90,99]
# l = (set(a))
# s = l.remove(max(l))


# s = 'hello'
# s1 = 'how are you'
# s2 = list(set(s) & set(s1))
# for i in s2:
#     print('common repeated letters are :',i)

# import requests
#
# res = requests.get('http://127.0.0.1:8000/-----')
# print(res.json())




# def polindrum(name):
#     reversedname = name[::-1]
#     if name ==reversedname:
#         print('polindrum')
#     else:
#         print('not polindrum')
# polindrum('radar')

#
# # x = open('D:/anitha.txt','w')
# # x.write('hello this is iam creating anitha file')
# # x.close()
# # print(x)
# # z = open('D:/anitha.txt','r')
# # print(z.read())
# # z.close()
#
#
# l = open('D:/anitha.txt','a')
# print(l.write('our family wisting our channal annaiah'))
# l.close()

# l = ['manas','bala','isantvik','malli','ramu','dhana']
# m = [i for i in l if i[0] in 'm']
# print(list(m))
# print(list(filter(lambda x:x[0] in 'aeiou',l)))
# k = [i for i in l if i[0] in 'aeiou']
# print(k)
# l = ['manas','bala','isantvik','malli','ramu','dhana','nsmdhsjhsjdhs','wuwwkjwjds']
# m = [i for i in l if len(i)>3 and not len(i)>4]
# print(m)
#
# z = list(filter(lambda x:len(x)>4 and not len(x)>10,l))
# print(z)

# l = [-3,12,65,4,66,7,60,90,-6,-10]


# start database------------> mongod
# create database-----------> use db
# switch database ------->use db
# show currentdatabase------->db
# show all database---------> show dbs (or) show databases
# create clooection---------> db.createCollection('employee')
# show collections -----------> show colllections
# drop database --------->db.dropDatabase()
# drop collection---------> db.employee.drop()
# db.employee.insertOne({'eno':1001},'name':'vijay')
# db.employee.find.pretty()
# update collection --------> db.employee.updateOne({'name':'vijay'},{$set:{'name':'anitha'}}))

#####################################################################################################################33
# and operator using django ORM
# employee.objects.filter(fname_startswith='R' , lname_startswith='M')
# employee.objects.filter(fname_startswith='R') & employee.objects.filter(lname_startswith='M')
# SELECT * FROM EMPLOYEE WHRER name LIKE 'R%' and name Like 'M%';
# employee.objects.order_by('salary')[2]
# SELECT * FROM EMPLOYEE ORDER_BY NAME ASC;
# SELECT * FROM EMPLOYEE ORDER_BY NAME DESC;
# EMPLOYEE.OBJECTS.ALL().AGGREGATE(AVG('AGE'))


# the encapsylation is the process of the to binding the data and mathos within singe unit
# the combination of data means the combination of vriable and methods with in single unit which is restrict in class
# Public : inside and outside of the class can be access data
# Protect : inside and child class can access data
# Privete : only inside can access data



# git congig user.email<email>
# git congig --global user.name<username>
# git clone <http://3fndjdhfjdy868787fdfd7fdfd79d8f9d89dv>
# git status
# git add .
# git commit -m 'change the item in the code line number 34'
# git pull
# git push
# git log used to check the previous code
# git branch branchname
# git checkout <branch name>
# git diff
# git branch -d <branch name>
# git checkout<git token can provided>



# class Human:
#     def walk(self):
#         print('walking is called')
#     def ramp(self):
#         print('ramp will called')
#
# if __name__ == '__main__':
#     onj = Human()
#     onj.ramp()