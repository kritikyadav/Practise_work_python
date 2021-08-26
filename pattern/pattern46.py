n=int(input('rows= '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n-j+1,end='')
    for l in range(n-i,0,-1):
        print(n-i+1,end='')
    print()
