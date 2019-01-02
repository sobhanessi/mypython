

def anagrams(s1,s2):

    l = []
    g = []

    if len(s1) == len(s2):
    
        for i in range (0,len(s1)):

            l.append(s1[i])
            

        for i in range (0,len(s2)):

            g.append(s2[i])
            

            
        l.sort()
        print(l)
        g.sort()
        print(g)
        
        if l == g :
            print("ham khanevade hastan ina")
    
        else:
            for i in l:
                if i in g:
                    l = l.remove(i)
                    g = g.remove(i)
                    continue
                elif (len(l) and len(g)) == 0:
                    print("man inja hastam va ham khanevade")
                    break
                else:
                    print("ina yeki nistan ke")
                    break
    else:

        print("ina ke barabar nistan")
        



s1 = input("enter your fucking string : ")       
s2 = input("enter your second ducking string : ")

anagrams(s1,s2)
