#def single insert or delete

def single_insert_or_delete(s1,s2):

    if s1 == s2 :
        return 0
    elif  (len(s1) + 1 == len(s2)) or (len(s1) == len(s2) + 1):
        return 1
    else:
        return 2
