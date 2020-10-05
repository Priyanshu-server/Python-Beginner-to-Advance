data = input("Enter Something :: ")

f = open("data.txt","w")
f.write(data)
f.close()