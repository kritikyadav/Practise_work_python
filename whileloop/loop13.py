n=int(input("Enter a number: "))
s=0
while n>0:
    a=n%10
    s=s+a
    n=n//10
print("The sum of digits is: ",s)
