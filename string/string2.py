#WAP to reverse order of words
s=str(input('enter string: '))
s1=s.split()
s2=s1[::-1]
s3=" ".join(s2)
print(s3)
