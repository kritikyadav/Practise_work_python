l1=[]
l2=[]
p=1
l1=[int(i) for i in input('enter string: ').strip().split()]
s1=set(l1)
l2=list(s1)
print('unique element in list are: ',l2)
for x in l2:
    p=p*x
print('product is: ',p)
