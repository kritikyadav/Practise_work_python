n=int(input("Enter a number: "))
i=1
s=0
while i<=n:
    if i%2==0:
        s=s+i
    i=i+1
print('sum of all even no.= ',s)
