#find single insert or delete characters

def single_insert_or_delete(s1,s2):

    if(s1 == s2):

        print("0")

    elif((len(s1) == len(s2)+1) or (len(s2) == len(s1)+1)):

        print("1")

    else:

        print("2")


s1 = input("enter s1 pls : ")

s2 = input("enter s2 pls : ")

single_insert_or_delete(s1,s2)

