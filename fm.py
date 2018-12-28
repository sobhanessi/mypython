#find mismatch characters

def find_mismatch(s1,s2):

    if(s1 == s2):

        print("0")

    elif(len(s1) == len(s2)):

        print("1")

    else:

        print("2")


s1 = input("enter s1 pls : ")

s2 = input("enter s2 pls : ")

find_mismatch(s1,s2)

