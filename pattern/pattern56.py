n=int(input('rows= '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end='')
    for k in range(i-1,0,-1):
        print(k,end='')
    print()
for i in range(1,n):
    for j in range(1,n-i+1):
        print(j,end='')
    for k in range(n-i-1,0,-1):
        print(k,end='')
    print()
