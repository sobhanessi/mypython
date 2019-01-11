#find mismatch characters

def find_mismatch(s1,s2):

    if(s1 == s2):

        return 0

    elif(len(s1) == len(s2)):

        return 1

    else:

        return 2


#s1 = input("enter s1 pls : ")

#s2 = input("enter s2 pls : ")

#mismatch = find_mismatch(s1,s2)

#print("mismatch",mismatch)
