n=int(input('enter the nu. of rows= '))
for i in range(n,0,-1):
    for j in range(1,1+i):
        print(n-j+1,end='')
    print()
