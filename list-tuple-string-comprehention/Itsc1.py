l1=[]
l1=[int(i) for i in input('enter elements of list: ').strip().split()]
l1[0],l1[-1]=l1[-1],l1[0]
print(l1)
