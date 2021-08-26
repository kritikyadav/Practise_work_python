n=int(input('enter number of rows: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j==1 or i==1 or j==n or i==n) and not (j==1 and i==1) and not (j==n and i==1) and not (j==1 and i==n)and not(j==n and i==n):
            print("1",end='')
        else:
            print("0",end='')
    print()
