user_name='vijay'
password=12345

u_name=input('enter your name')
u_password=int(input('enter password'))

if u_name==user_name and u_password==password:
    print('''
    1.deposite
    2.withdreaw
    3.ministatement
    4.exit
    ''')
    amount=50000
    option=int(input('enter any option'))
    if option==1:
        dep=int(input('enter amount'))
        amount+=dep
        print('total amount:::',amount)
    elif option==2:
        withd=int(input('enter amount'))
        amount-=withd
        print('total amount:::',amount)
    elif option==3:
        print('<------ATML------->')
        print('user_name:::',user_name)
        print('total_amount:::',amount)
        print('Thankyou For Visit')
    elif option==4:
        print('exit')
    else:
        print('enter valid details')
