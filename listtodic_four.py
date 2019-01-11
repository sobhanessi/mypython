def list_to_dic(f):

    fp = open(f,'r')

    data = fp.readlines()

    dic = {}
    dic['milk'] = []
    dic['bread'] = []
    
    for i in data:

        n,a,b,c = i.strip('\n').split()

        if n == 'm':

            dic['milk'] = dic['milk'] + [float(a),float(b),float(c)]

        else:

            dic['bread'] = dic['bread'] + [float(a),float(b),float(c)]
        
                
    print(dic)


       
f = 'text4.txt'

list_to_dic(f)
