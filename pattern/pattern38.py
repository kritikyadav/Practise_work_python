n=int(input('enter number of rows: '))
t=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if t%2==0:
            print("0",end='')
        else:
            print("1",end='')
        t+=1
    print()
