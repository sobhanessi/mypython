#shomare baraye sanad zadan haye rasmi va gheyre rasmi

#jahate yad avari:

#1.yadam bashe baad az inke barname khast amali beshe, baraye
#LOG giri ham datetime ro ham rah ba esme karbar write konam too yek file dg..

#2.

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
    




def rasmi():


    fp = open("rasmi.txt",'r+')

    data = fp.readlines()
    z = 0
    
    for i in data:
        z = int(i)

    print("adade rasmi e shoma hast = {0:<5d}".format(z))

    z = z + 1
    z = str(z)

    fp.seek(0)
    fp.truncate()

    fp.write(z)
    fp.close()





    
gheyre_rasmi()
rasmi()

    

    
