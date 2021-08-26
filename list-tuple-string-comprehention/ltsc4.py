l1=[]
l1=[i for i in input('enter string: ').strip().split()]
s=input("enter item: ")
for i in l1:
    if i==s:
        print("element found")
        break
else:
    print("not")
