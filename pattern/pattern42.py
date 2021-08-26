n=int(input('enter number of rows: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==(n//2)+1 and i==(n//2)+1:
            print("0",end='')
        else:
            print("1",end='')
    print()
