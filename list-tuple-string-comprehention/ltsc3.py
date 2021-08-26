l1=[]
l2=[]
l1=[i for i in input('enter elements of list: ').strip().split()]
for x in l1:
    s=''
    for i in x:
        if i=='e':
            s=s+'g'
        elif i=='g':
            s=s+'e'
        else:
            s=s+i
    l2.append(s)
print(l2)

        
