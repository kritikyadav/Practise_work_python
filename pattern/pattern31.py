n=int(input('enter number of rows= '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i==1 or i==n or j==1 or j==n):
            print('1',end='')
        else:
            print('0',end='')
    print()
