import csv
with open("emp.csv","r") as f:
    data=csv.reader(f)
    r=list(data)
    for i in r:
        for j in i:
            print(j,end='\t')
        print()
