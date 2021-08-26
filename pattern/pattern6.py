n=int(input('enter number of rows: '))
for i in range(1,n+1):
    for j in range(i+1,1,-1):
        print(j-1,end='')
    print()
