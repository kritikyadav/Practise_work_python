n=int(input('no. of rows: '))
for i in range(1,n+1):
    for j in range(2*i-1,2*n-1,2):
        print(j,end='')
    print()
