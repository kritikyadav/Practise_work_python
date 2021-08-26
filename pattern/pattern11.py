n=int(input('enter number of rows: '))
t=65
for i in range(1,n+1):
    for j in range(1,1+i):
        print(chr(t),end='')
        t+=1
    print()
