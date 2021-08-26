#!/usr/bin/env python
# coding: utf-8

# In[4]:


def fact(a):
    for i in range(1,a):
        a=a*i
    return(a)

n=int(input('enter number: '))
ans=fact(n)
print(f"factorial of {n} is: {ans}")


# In[1]:


def prime(a):
    for i in range(2,a//2+1):
        if(a%i==0):
            print("number is not prime")
            break
    else:
        print("Prime number")
    
n=int(input('enter number: '))
prime(n)


# In[11]:


def swap(a,b):
    a,b=b,a
    return a,b
n1=int(input('enter number1: '))
n2=int(input("enter number2: "))
x,y=swap(n1,n2)
print('swaped numbers are:',x,y)


# In[24]:


def power(a,b):
    p=a**b
    return(p)
n1=int(input('enter number: '))
n2=int(input('enter power: '))
ans=power(n1,n2)
print('swaped numbers are:',ans)


# In[1]:


def type(a):
    if(a%2==0):
        print("even number")
    else:
        print("odd number")
a=int(input("enter a number: "))
type(a)


# In[2]:


def cal(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)   
a=int(input("enter a number: "))
b=int(input("enter a number: "))
ans=cal(a,b)


# In[3]:


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
choice=int(input('''enter 1 to add
2 to sub
3 to mul
4 to div'''))
if choice==1:
    ans=add(a,b)
elif choice==2:
    ans=sub(a,b)
elif choice==3:
    ans=mul(a,b)
elif choice==4:
    ans=div(a,b)


# In[3]:


def armstrong(a):
    old=a
    cnt=len(str(a))
    sum=0
    while a>0:
        s=a%10
        sum=sum+(s**cnt)
        a=a//10
    if sum==old:
        print("Armstrong number")
    else:
        print("not armstrong number")
a=int(input("enter a number: "))
armstrong(a)


# In[18]:


def perfect(a):
    old=a
    sum=0
    for i in range(1,a//2+1):
        if a%i==0:
            sum+=i
    if sum==old:
        print("perfect number")
    else:
        print("not a perfect number")
a=int(input("enter number: "))
x=perfect(a)


# In[3]:


def strong(a):
    old=a
    sum=0
    while a>0:
        s=a%10
        f=1
        for i in range(1,s+1):
            f=i*f
        sum=sum+f
        a=a//10
    if sum==old:
        print("strong number")
    else:
        print("not a strong number")
a=int(input("enter number: "))
x=strong(a)


# In[5]:


def sum ():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a+b;

ans=sum()
print("Sum = ",ans)


# In[6]:


def sum (a,b):
    return a+b;
a = int(input("Enter a: "))
b = int(input("Enter b: "))
ans=sum(a,b)
print("Sum = ",ans)


# In[2]:


def cube(a):
    return a**3;
a = int(input("Enter a: "))
ans=cube(a)
print("cube = ",ans)


# In[3]:


def area(r):
    return 3.141*r*r;
r = int(input("Enter radius: "))
ans=area(r)
print("area of circle = ",ans)


# In[10]:


def mxmn(a,b):
    if(a>b):
        print(f"{a} is max, {b} is min")
    else:
        print(f"{b} is max, {a} is min")
a=int(input("enter first number: "))
b=int(input("enter second number: "))
ans=mxmn(a,b)


# In[8]:


def evod(a):
    if(a%2==0):
        print("even number")
    else:
        print("odd number")
a=int(input("enter first number: "))
ans=evod(a)


# In[28]:


def type(a):
    i=0
    
    '''prime'''
    
    for i in range(2,a//2+1):
        if a%i==0:
            break
    else:
        print("prime number")
    
    '''armstrong'''
    
    l=len(str(a))
    arm=a
    sum=0
    while(arm!=0):
        n=arm%10
        sum=sum+n**l
        arm=arm//10
    if sum==a:
        print("armstrong number")
    
    '''perfect'''
    
    old=a
    sum=0
    for i in range(1,a//2+1):
        if a%i==0:
            sum+=i
    if sum==old:
        print("perfect number")
    
a=int(input("enter first number: "))
type(a)


# In[31]:


def prime(a,b):    
    for i in range(a,b+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            print(i)

a=int(input("enter starting number: "))
b=int(input("enter end number: "))
prime(a,b)


# In[6]:


def strong(a,b):
    for j in range(a,b+1):
        old=j
        sum=0
        while old>0:
            s=old%10
            f=1
            for i in range(1,s+1):
                f=i*f
            sum=sum+f
            old=old//10
        if sum==j:
            print(j)

a=int(input("enter start number: "))
b=int(input("enter ending number: "))
strong(a,b)


# In[1]:


def arm(a,b):    
    for i in range(a,b+1):
        l=len(str(i))
        ar=i
        sum=0
        while(ar!=0):
            n=ar%10
            sum=sum+n**l
            ar=ar//10
        if sum==i:
            print(i)

a=int(input("enter starting number: "))
b=int(input("enter end number: "))
arm(a,b)


# In[2]:


def perfect(a,b):    
    for i in range(a,b+1):
        old=i
        sum=0
        for j in range(1,i//2+1):
            if i%j==0:
                sum+=j
        if sum==old:
            print(j)

a=int(input("enter starting number: "))
b=int(input("enter end number: "))
perfect(a,b)


# In[ ]:




