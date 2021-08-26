b=0
brs=0
c=0
crs=0
r=0
rrs=0
def bus():
    global b
    b+=1
    global brs
    
    brs=100*b
def cycle():
    global c
    c+=1
    global crs
    crs=c*20
def riksha():
    global r
    r+=1
    global rrs
    rrs=r*50
def status():
    print(f'''
Number of Bus: {b}
Number of Cycle: {c}
Number of Riksha: {r}
Total Vehicle: {b+c+r}
Total Amount(Rs): {brs+crs+rrs}''')
