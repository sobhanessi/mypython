#tamrine 6 dic


def dic(s,n):

    k = s.keys()
    l = []

    for i in k:

        if n in s[i]:

            l.append(i)

    print(l)




s = {"rabbit" : [1, 2, 3],"kitten" : [2, 2, 6],"lioness": [6, 8, 9]}

n = 9

dic(s,n)




            
        
