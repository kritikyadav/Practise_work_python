def prime(a):
    p=1
    for i in range(2,a//2+1):
        if(a%i==0):
            print("number is not prime")
            break
    else:
        print("Prime number")
    
n=int(input('enter number: '))
ans=prime(n)
