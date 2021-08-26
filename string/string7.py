s=str(input('enter string: '))
s2=''
for i in range(0,len(s),2):
    s2=s2+(s[i]+chr(ord(s[i]) + int(s[i+1]) ) )
print(s2,end='')
