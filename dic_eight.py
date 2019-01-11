
def dic(s):

    s.lower()
    dic = {}

    l = ['a','o','i','e','u']

    for i in s:

        if(i != " ") and (i in l):

            if i not in dic:

                n = s.count(i)
                dic[i] = n


    print(dic)



s = "salam man ham inja hastam o mikhastam bebinam chandta u inja hast ke ghaedatan bayad ye doone bashe"

dic(s)
