l1=[]
l1=[int(i) for i in input('enter string: ').strip().split()]
print(l1)
l2=[]
s1=[l2.append(x) for x in l1 if x not in l2]
print('unique element in list are: ',l2)
