n=int(input('enter number = '))
p=1
while n>0:
    a=n%10
    n=n//10
    p=p*a
print('Product of digits = ',p)
