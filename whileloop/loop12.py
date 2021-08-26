n=int(input('enter no. = '))
i=1
while i<=n:
    if i%2==0:
        print(i-1,end='\t')
    else:
        print(i+1,end='\t')
    i+=1
