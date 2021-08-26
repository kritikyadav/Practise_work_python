n=int(input('enter number= '))
i=1
while i<=n:
    if i%2==0:
        print('0',end='\t')
    else:
        print('1',end='\t')
    i+=1
