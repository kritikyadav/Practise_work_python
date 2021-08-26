n=int(input('enter the number of rows= '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j+n-i,end='')
    for l in range(n-i,0,-1):
        print(l,end='')
    print()
