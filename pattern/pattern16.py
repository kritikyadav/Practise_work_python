n=int(input('enter number of rows: '))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(chr(j+96),end='')
    print()
