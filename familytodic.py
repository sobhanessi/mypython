#tabdile asami be dic

def fdic(f):

    dic = {}

    file = open(f,'r')

    data = file.readlines()

    for i in data :

        fn,ln,age = i.strip('\n').split(',')

        if ln not in dic:

            dic[ln] = {fn:int(age)}
            
        else:

            if fn not in dic[ln]:
                dic[ln][fn] = int(age)


    print(dic)




f = 'text5.txt'

fdic(f)

