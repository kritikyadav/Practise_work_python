def armstrong(a):
    old=a
    cnt=0
    while a!=0:
        a=a//10
        cnt+=1
    sum=0
    a=old
    while a!=0:
        s=a%10
        sum=sum+(s**cnt)
        a=a//10
    if sum==old:
        print("Armstrong number")
    else:
        print("not armstrong number")
a=int(input("enter a number: "))
x=armstrong(a)
