s=str(input('enter string: '))
l=[]
j=0
s1=''
for i in range(len(s)):
    if s[i] not in l:
        l.append(s[i])
s1=''.join(l)
print(s1)
