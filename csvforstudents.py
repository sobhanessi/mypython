#first_name,math,physics,chemistry,biology

def csv_to_dict_for_students(f):

    fp = open(f,'r')

    data = fp.readlines()

    dic = {}
    ad = {}

    for i in data:

        fn,math,physics,chemistry,biology = i.strip('\n').split(',')

        if float(math) > 70 and float(chemistry) > 70:

            dic[fn] = [float(math),float(physics),float(chemistry),float(biology)]
        
                
    print(dic)


       
f = 'text3.txt'

csv_to_dict_for_students(f)
