n=int(input("Enter a number: "))
t=n
r=0
while n>0:
    a=n%10
    n=n//10
    r=(10*r)+a
if r==t:
    print('palindrome no.')
else:
    print('not palindrome')
