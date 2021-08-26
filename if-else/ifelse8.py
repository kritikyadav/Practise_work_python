a=int(input('enter 3 digit no. = '))
b=a%10 
x=a//10 
c=x%10  
d=x//10 
n=b*100+c*10+d
print('reverse no.= ',n)
if a==n:
    print('no. is palindrome')
else:
    print('no. is not a palindrome')
