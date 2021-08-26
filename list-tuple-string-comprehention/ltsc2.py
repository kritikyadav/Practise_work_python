l1=[]
l1=[int(i) for i in input('enter elements of list: ').strip().split()]
print ([list((i, l1[i])) for i in range(len(l1))])
f=int(input('enter index of first element:'))
s=int(input('enter index of second element:'))
l1[f],l1[s]=l1[s],l1[f]
print(l1)
