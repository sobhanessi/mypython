#list ha be onvane maghadir dar dict


def lbm(dic):

    k = dic.keys()
    l = []
    
    
    for i in k:

        nomre = dic[k]
        n1,n2,n3 = nomre[0], nomre[1], nomre[2]

        if n1+n2+n3 >= 78:
            l.append(k)
    return l


dic = {'ali':[15,18,20],"mohsen":[18,15,10],"parnaz":[20,19.5,19.75]}

lbm(dic)

