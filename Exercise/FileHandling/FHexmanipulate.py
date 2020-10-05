f = open("data.txt","r")
data = f.read()
f.close()
trans = ""

for letter in data:
    if letter in "aeiou":
        trans = trans + "p"

    else:
        trans = trans + letter


f = open("data.txt","w")
f.write(trans)