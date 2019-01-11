def dic_twelve(n):

    dic_yekan = {1 : "one",2 :"two", 3 : 'three', 4 : 'four', 5 : 'five', 6 : 'six', 7 : 'seven',
           8 : 'eight', 9 : 'nine' , 10 : 'ten', 11 : 'eleven', 12 : 'twelve',
           13 : 'thirteen', 14 : 'fourteen',15 :  'fifteen',
           16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen', 19 : 'nineteen'}
    dic_dahgan = {
           
           2 : 'twenty',3 : 'thirty',4: 'forty',5 : 'fifty',6 : 'sixty',
           7 : 'seventy', 8: 'eighty',
           9 : 'ninety'}
    dic_sadgan = {
           100 : 'hundred'}
    dic_hezargan = {
           1000 : 'thousand'}

    
       

    k = ""
    
    if n > 1000:

        z = int(n/1000)
        h = n%1000
        k = dic_yekan[z] + " " + dic_hezargan[1000] + " "
        
        
        if h > 100:

            z = int(h/100)
            l = h%100
            k = k + dic_yekan[z] + " " + dic_sadgan[100] + " "
            

            if l >= 10:

                z = int(l/10)
                m = l%10
                print(z,m)
                if m == 0 and z > 0:
                    
                    k = k + dic_dahgan[z]
                    print(k)

                elif (m > 0 and m < 10) and z > 0:

                    k = k + dic_dahgan[z] + " " + dic_yekan[m]
                    print(k)
                else:
                    
                    k = k + dic_yekan[z]
                    print(k)
            elif l < 10 and l > 0:

                k = k + dic_yekan[l]

            else:

                
                print(k)
                
                    
        elif h < 20:

            k = k + dic_yekan[h]

    
        print(k)
    

n = 9900

dic_twelve(n)
