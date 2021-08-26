n=int(input('rows= '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=' ')
    for k in range(1,i+1):
        print(n-k+1,end='')
    for l in range(i,1,-1):
        print(n-l+2,end='')
    print()
for i in range(1,n):
    for j in range(1,i+1):
        print(end=' ')
    for k in range(n-i,0,-1):
        print(k+i,end='')
    for l in range(n-i-1,0,-1):
        print(n-l+1,end='')
    print()
