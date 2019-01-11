#nested list max for instance#
#barname eslah shod va dorost hast


def nested_max(l):
	
    even_max = 0
    o = []
    for i in l:
        
        if type(i) == list:
            
            for j in range (0,len(i)):

                z = i[j]

                if (z%2 == 0) and (z > even_max):
                    
                    even_max = z
        else:
            
            if (i%2 == 0) and (i > even_max):
                even_max = i
            
                

    print(even_max)
        


l = [1,2,[3,12]]

p = nested_max(l)

