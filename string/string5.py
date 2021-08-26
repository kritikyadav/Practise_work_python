s1=str(input('enter string: '))
s2=s3=s4=''
for i in s1:
    if i.isalpha():
        s2=s2+i
    else:
        s3=s3+i
for i in sorted(s2):
    s4=s4+i
for i in sorted(s3):
    s4=s4+i
print(s4)
