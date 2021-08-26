n=int(input('rows= '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end='')
    for l in range(2*i-1,0,-1):
        print("*",end='')
    print()
for i in range(1,n-1):
    for j in range(1,n-1):
        print("*",end='')
    for l in range(1,n-1):
        print(end=' ')
    for k in range(1,n-1):
        print("*",end='')
    print()
