encrypt = {'a':2,'b':10,'c':20,'gh':32}

# for key,value in encrypt.items():
#     print(key)
#     print(value)

user_strng = input("enter your string :: ")
trans = ""

for letter in user_strng:
    for key,value in encrypt.items():
        if letter == key:
            trans = trans+str(value)

    else:
        trans= trans+letter

print(trans)
