a=int(input('year= '))
if a%4==0 and a%100==0:
    print('is a leap year')
elif a%4==0 and a%100!=0:
    print('is a leap year')
else:
    print('is not a leap year')
