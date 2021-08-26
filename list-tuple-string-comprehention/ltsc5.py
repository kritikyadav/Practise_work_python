l1=[]
l2=[]
l1=[int(i) for i in input('enter string: ').strip().split()]
s1=set(l1)
l2=list(s1)
print('unique element in list are: ',l2)
