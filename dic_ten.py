
def dic_ten(n):


    dic = {0:'zero',1:'one', 2:'two',3:'three',4:"four",
           5:'five',6:'six',7:"seven",8:'eight',9:'nine'
           }

    s = str(n)
    l = []
    for i in s:
        l.append(int(i))
        
    
    f = ""
    
    for i in l:

#        f = f + dic.pop(i) + " "
         f = f + dic[i] + " "
        
    print(f)

n = 4721

dic_ten(n)
