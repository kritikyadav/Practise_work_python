#WAP to reverse words in a string
s=str(input('string: '))
w=s.split()
nw=[word[::-1] for word in w]    
ns=" ".join(nw)
print(ns)
