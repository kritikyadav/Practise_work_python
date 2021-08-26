l=[1,2,3]
for i in l:
    for j in l:
        for k in l:
            if i!=j and i!=k and j!=k:
                print(i,j,k)
