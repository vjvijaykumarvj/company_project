a = int(input('enter number'))
if a>1:
    for i in range(2,a):
        if a%i == 0:
            print(a,'------>not prime number')
            break
    else:
        print(a,'------>Prime number')




