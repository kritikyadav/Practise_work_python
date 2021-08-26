def add(a,b):
    print("add=",a+b)
def sub(a,b):
    print("sub=",a-b)
def mul(a,b):
    print("mul=",a*b)
def div(a,b):
    print("div=",float(a)/b)   
a=int(input("enter a number: "))
b=int(input("enter a number: "))
choice=int(input('''enter a number (1 to 4)
1 to add
2 to sub
3 to mul
4 to div: '''))
if choice==1:
    ans=add(a,b)
elif choice==2:
    ans=sub(a,b)
elif choice==3:
    ans=mul(a,b)
elif choice==4:
    ans=div(a,b)
