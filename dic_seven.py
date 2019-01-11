
def dic(s):

    s.lower()
    s_new = s.strip()

    dic = {}

    for i in s_new:
        n = 0
        if i != " ":
            if i not in dic:
                n = s_new.count(i)

                dic[i] = n
    print(dic)

s = "salam chetori dadash"

dic(s)
