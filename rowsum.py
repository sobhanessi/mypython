#fehreste jam satr haye yek liste do bodi

def row_sum(l):

    sc = []
    sc1 = 0
    x = 0
    
    for i in l:
        z = 0
        if type(i) == list:
            x = x + 1
            for j in range (0,len(i)):
                z = i[j] + z
            sc.append(z)

        else:

            sc1 = sc1 + i
            

    
    sc.insert(0,sc1)


    for i in range (0,x+1):
        print("dar satre : ",i,"enghadr darim : ",sc[i])


l = [1,2,[3,4],5,6,[7,8],9]

row_sum(l)

