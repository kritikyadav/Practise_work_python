n=int(input('rows= '))
for i in range(n,0,-1):
    print(' '*(i-1),end='')
    for j in range(n,i-1,-1):
        print(n-j+1,end='')
    print()
