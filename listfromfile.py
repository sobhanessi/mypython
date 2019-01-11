#list from file

def list_from_file(file_name):
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    # NOW CONTINUE YOUR CODE FROM HERE!!!

    print(data)

    l = []

    for i in data:

        stripped = i.strip('\n')
        l.append(stripped)

    print(l)
    




file_name = 'text.txt'

list_from_file(file_name)

