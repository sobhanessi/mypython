#def find mismatch new

def find_mismatch(s1,s2):

    s1 = s1.lower()
    s2 = s2.lower()

    if (s1 == s2):
        return 0
    elif (len(s1) == len(s2)):
        return 1
    else:
        return 2

