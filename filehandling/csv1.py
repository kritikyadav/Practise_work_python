import csv
with open("emp.csv","a",newline='') as f:
    w=csv.writer(f)
    w.writerow(["Eno.","Ename","Esal","Eadd"])
    while True:
        Eno=int(input("enter eno.: "))
        Ename=input("enter E.Name: ")
        Esal=int(input("enter sal: "))
        Eadd=input("enter E.address: ")
        w.writerow([Eno,Ename,Esal,Eadd])
        option=input("Do you want to add more details[yes,no]:")
        if option.lower()=="no":
            break
        
print("Done")
