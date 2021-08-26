n=int(input("enter rows= "))
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print(end=' ')
    for l in range(2*(n-i)+1,0,-1):
        print("*",end='')
    print()
