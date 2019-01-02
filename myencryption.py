#encoding

def my_encryption(s):

    character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    secret_key = "Dd18Abz2EqNPW hYTOjBvtVlpXaH6msFUICg4o0KZwJeryQx3f9kSinRu5L7cGM"

    h = ""
    
   

    for i in range (0,len(s)):

        print("i am here ")

        b = character_set.find(s[i])

        h = h + secret_key[b]

    print(h)

s = input("string e khod ra vared konid : ")

my_encryption(s)
