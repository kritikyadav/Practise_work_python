n=int(input('enter the nu. of rows= '))
t=1
for i in range(1,1+n):
    for j in range(i,i+i):
        if t<10:
            print(t,end=' ')
        else:
            print(t%10,end=' ')
        t+=1
    print()
