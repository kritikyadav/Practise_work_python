n=int(input("Enter a number: "))
r=0
while n>0:
    a=n%10
    n=n//10
    r=(10*r)+a
print(r)
