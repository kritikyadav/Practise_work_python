def fact(a):
    for i in range(1,a):
        a=a*i
    return(a)

n=int(input('enter number: '))
ans=fact(n)
print(f"factorial of {n} is: {ans}")
