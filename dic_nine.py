
def dic(s):

    s = s.lower()

    print(s)

    dic = {}
    s_new = s.strip().split()

    for i in s_new:

        if i not in dic:

            n = s.count(i)
            dic[i] = n
            
    print(dic)


s = "I am tall when I am young and I am short when I am old"

dic(s)
