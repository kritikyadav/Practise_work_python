n=int(input('enter number: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (j==i or j==1 or i==n):
            print('1',end='')
        else:
            print('0',end='')
    print()
