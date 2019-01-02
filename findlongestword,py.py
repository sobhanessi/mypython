#def find longest word

def flw(s):

    s_new = s.split("s")

    z = 0
    k = ""

    print(s_new)
    
    for i in s_new:

        if len(i) > z:
            z = len(i)
            k = i
        else:
            continue

    return k,z


s = input("enter your strings : ")

m = flw(s)

print(m)
