def swap(a,b):
    a,b=b,a
    return a,b
n1=int(input('enter number1: '))
n2=int(input("enter number2: "))
x,y=swap(n1,n2)
print('swaped numbers are:',x,y)
