#def spelling corrector

from findmismatch import find_mismatch
from singleinsertordelete import single_insert_or_delete

def spelling_corrector(s1,l):
    s1 = s1.lower()
    l = l.lower()
    
    l_list = l.split()
    s1_list = s1.split()

    g = ""
    
    for i in s1_list:
        if len(i) <= 2 :
            g = g + i + " "
            print("i am in 1")
            continue
        else:
            for j in l_list:
                fm = find_mismatch(i,j)
                if fm == 0:
                    g = g + i + " "
                    print("i am in 2")
                    break
                
                elif fm == 1:
                    si = single_insert_or_delete(i,j)
                    if si == 1:
                        g = g + j + " "
                        print("i am in 3")
                        break
                    else:
                        g = g + i + " "
                        print("i am in 4")
                        break
                    
                else:
                    g = g + i + " "
                    print("i am in 5")
                    break
                
            
        print(g)
                    
        






s1 = input("lotfan reshteye morede nazar ra vared konid : ")
l = input("lotfan liste kalamate sahih ra vared konid : ")

sp = spelling_corrector(s1,l)
print(sp)
