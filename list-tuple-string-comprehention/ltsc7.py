l1=[]
l1=[int(i) for i in input('enter string of numbers: ').strip().split()]
l2=[]
s1=[l2.append(x) for x in l1 if x not in l2]
for x in l2:
    if l1.count(x)==3:
        print('number repeating three times: ',x)

