n=int(input('enter number of rows: '))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(j-i+5,end='')
    print()
