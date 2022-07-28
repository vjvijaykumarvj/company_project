#Swap Method::::::
'''
x=10
y=20
x,y=y,x
print('x--->',x)
print('y--->',y)
'''
'''x=10
y=20
temp=x
x=y
y=temp
print('x--->',x)
print('y--->',y)
'''


'''def polindram(string):
    reversed=string
    if string ==reversed[::-1]:
        print('its polindram')                #polindram by using Functions
    else:
        print('not polindram')
polindram('MADAM')
'''

'''string =input('enter name')
if string==string[::-1]:
    print('polindram')                     #polindram using normal method
else:
    print('no polindram')
'''

#sepatate the string and integers values :::::
'''numbers=[]
names=[]
list=['vijay',123,'anitha',44343,'subramanyam','eswaramma',4343,343,43,2,3,12.3,34.32,43.4]
for i in list:
    if type(i)==str:
        names.append(i)
    if type(i)==int:                                             #sepatate the string and integers values :::::
        numbers.append(i)
        
print('names:::',names)
print('numbers:::',numbers)
'''

#Zip Functions::::

'''list1=['a','b','c']
list2=[10,20,30]                     $Zip Functions
print(list(zip(list1,list2)))
'''

'''names=['mansa','apple','enasa','ramu','ice','ball']
y=filter(lambda x:x[0] in 'a,e,i,o,u', names)               #find out the 'a,e,i,o,u' in using Filter functions
print(list(y))
'''
'''names=['mansa','apple','enasa','ramu','ice','ball']
y=[name for name in names if name[0] in 'a,e,i,o,u']            # find out the 'a,e,i,o,u' by using comprehension methos
print(list(y))
'''

'''names=['mangodb','c','c++','java''python','casendra','oracle','arc']
x=list(filter(lambda name:len(name)>3 and name[1]=='a',names))            #find oyt the length and posion of the charecter by usingfilter and lambda function
print(x)
'''

'''names=['mangodb','c','c++','java''python','casendra','oracle','arc']
x=[name for name in names if len(name)>3 and name[1]=='a']                #find oyt the length and posion of the charecter by using comprehension functions
print(list(x))
'''

#Anagram check 2 string are same are not:::
'''def anagram(s1,s2):
    return set(s1)==set(s2)                       #Anagram check 2 string are same are not:::
x=anagram('namma','manam')
print(x)
'''

#remove the duplicate from the list::
'''s=list(range(10))+list(range(10))
st=list(set(s))                                 #remove the duplicate from the list::
print(st)
'''

#febonacii therom
'''a,b=1,0
n=12
for e in range(n):                       #febonacii therom 
    print(b)
    a,b=b ,a+b
'''

'''number=2
value=5
for value in range(1,1+value):
    print(number,'*',value,'=',number*value)
'''

'''number=int(input('enter any number'))
value=int(input('enter any value'))                  #Table method using 
for value in range(1,1+value):
    print('{}*{}={}'.format(number,value,number*value))
'''
#Hoe to concatinate of 2 tuples:::
'''tuple1=(1,2,3,4,5)
tuple2=(6,7,8,9,10)
t=tuple1+tuple2
print(t)

tup1=(1,'a',True)
tup2=(4,5,6)
tup3=tup2+tup1
print(tup3)
'''

'''#Remove the duplicate elements of the list by using dict method
list1=['a','b','b','c','d','a']
print(list(dict.fromkeys(list1)))

#Remove the duplicate elements by using set method:::
list1=['a','b','b','c','d','a']
print(list(set(list1)))
'''


