n=int(input('enter the nu. of rows= '))
for i in range(n,0,-1):
    for j in range(i,i+i):
        print(i,end='')
    print()
