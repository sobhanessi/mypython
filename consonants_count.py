#def count consonants

def count_consonants(s):

    s = s,lower()
    
    vs = ['a','e','i','o','u']

    count = 0
    
    for i in range(0,len(s)):
        if s[i] in vs:
            continue
        else:
            count = count + 1

    return count

s = input("un reshteye laanatit ro benevis : ")

c = count_consonants(s)
print(c)
