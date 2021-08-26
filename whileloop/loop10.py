n=int(input('enter number= '))
i=1
while i<=n:
    if i%2==0:
        print(-(2*i-1),end='\t')
    else:
        print(2*i-1,end='\t')
        
    i+=1
    
