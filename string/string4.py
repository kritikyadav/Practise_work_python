s1=str(input('enter string1: '))
s2=str(input('enter string2: '))
i,j=0,0
s3=""
while i<len(s1) or j<len(s2):
    if i<len(s1):
        s3=s3+s1[i]
        i+=1
    if j<len(s2):
        s3=s3+s2[j]
        j+=1
print(s3)   
