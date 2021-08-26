n=int(input("enter rows= "))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(end=' ')
    for l in range(0,2*i-1):
        print(l+1,end='')
    print()
