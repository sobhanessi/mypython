#shomare baraye sanad zadan haye rasmi va gheyre rasmi

import jdatetime

def gheyre_rasmi():

    d = jdatetime.date.today()
    
    fp = open("gheyre_rasmi.txt",'r+')

    data = fp.readlines()
    z = 0
    
    for i in data:
        z = int(i)

    y = d.year
    if y > 1400:
        y = y -1400
    if y >= 1397 and y < 1400:
        y = y - 1300
    
    m = d.month
    sm = ""
    if m <= 3 and m >= 1:
        sm = "b"
    elif m <= 6 and m >= 4:
        sm = "t"
    elif m <= 9 and m >= 7:
        sm = "p"
    else:
        sm = "z"
    
    print("adade gheyre rasmi = {0:2d}_{1:1s}_{2:<5d}".format(y,sm,z))

    z = z + 1
    z = str(z)
    
    fp.seek(0) #ba in kar miaramesh sare khat
    
    fp.truncate() #ba in ham pakesh mikonam
    
    fp.write(z)
    fp.close()
    

gheyre_rasmi()

    

    
