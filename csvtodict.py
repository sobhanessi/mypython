# Type your code here

def csv_to_dict(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!

    dic = {}
    print(data)

    for i in data:
        n,g1,g2,g3,g4 = i.strip('\n').split(',')
        dic[n] = [float(g1),float(g2),float(g3),float(g4)]
        

    print(dic)

    



file_name = 'text2.txt'

csv_to_dict(file_name)

