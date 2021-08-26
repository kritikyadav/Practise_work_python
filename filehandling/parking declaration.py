from parkingmodule import*
n=0
while(n!=6):
    n=int(input('''
1. Enter Bus 
2. Enter Cycle 
3. Enter Riksha
4. Show Status
5. Delete Record
6. EXIT
'''))
    if n==1:
        bus()
    elif n==2:
        cycle()
    elif n==3:
        riksha()
    elif n==4:
        status()
    elif n==5:
        b=c=r=rrs=brs=crs=0
    elif n==6:
        print("Thank You")
        break
    else:
        print("INVALID INPUT,please try again")


