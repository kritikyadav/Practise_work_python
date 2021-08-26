#!/usr/bin/env python
# coding: utf-8

# In[4]:


def pow(a,b):
    if b==1:
        return a
    else:
        return(a*pow(a,b-1))
a=int(input("number= "))
b=int(input("power= "))
ans=pow(a,b)
print(ans)


# In[6]:


def num(i,n):
    if i<=n:
        print(i)
        num(i+1,n)
        return
    
n=int(input("number= "))
i=1
num(i,n)


# In[4]:


def even(num1,num2):
    if num1>num2:
        return
    print(num1,end=" ")
    return even(num1+2,num2)
def odd(num3,num2):
    if num3>num2:
        return
    print(num3,end=" ")
    return odd(num3+2,num2)
    
num1=2
num2=int(input("Enter your Limit:"))
print("even numbers are: ")
even(num1,num2)
num3=1
print("\nodd numbers are: ")
odd(num3,num2)


# In[7]:


def sum_Num(n):
    if n<= 1:
        return n
    else:
        return n+ sum_Num(n-1)
num=int(input("Enter a number: "))
if num < 0:
    print("Enter a positive number")
else:
    print("The sum is :",sum_Num(num))


# In[11]:


def SumEven(num1,num2):
    if num1>num2:
        return 0

    return num1+SumEven(num1+2,num2)
def sumodd(num3,num2):
    if num3>num2:
        return 0

    return num3+sumodd(num3+2,num2)
num1=2
print("Enter your Limit:")
num2=int(input())
print("Sum of all Even numbers in the given range is:",SumEven(num1,num2))
num3=1
print("Sum of all odd numbers in the given range is:",sumodd(num3,num2))


# In[2]:


def rev(n):
    global sum
    if n>0:
        r=n%10
        sum=(sum*10) + r
        rev(n//10)
        return sum

n=int(input("enter number: "))
sum=0
ans=rev(n)
print(ans)


# In[9]:


def rev(n):
    global sum
    if n>0:
        r=n%10
        sum=(sum*10) + r
        rev(n//10)
        return sum

a=int(input("enter number: "))
sum=0
ans=rev(a)
if ans==a:
    print("palindrome")
else:
    print("not palindrome")


# In[13]:


def sum(n):
    if n==0:
        return 0
    else:
        return n%10+sum(n//10)
n=int(input("enter number"))
ans=sum(n)
print(ans)


# In[1]:


def fact(n):
    if (n==0):
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter number: "))
ans=fact(n)
print(ans)


# In[4]:


def fibo(n):
    if(n==0 or n==1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
n=int(input("enter number: "))
ans=fibo(n)
print(ans)


# In[ ]:




