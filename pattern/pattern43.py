n=int(input('enter no. of rows= '))
for i in range(n,0,-1):
    for l in range(1,n-i+1):
        print(n-l+2-i,end='')
    for j in range(1,i+1):
        print(j,end='')
    print()    
