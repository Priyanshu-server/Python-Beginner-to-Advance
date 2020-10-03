# f = open("filehandlingpart2.txt","r")
# print(f.read(3)) #inside read you can give int argument which is equal to no. of chars you want to read.
# f.close()
# print(f.readline())
# for line in f:
#     print(line + " --<")

# f = open("filehandlingpart2.txt","w") #a for append #w for write
# f.write("xDoramming")
# f = open("filehandlingpart2.txt","a") #a for append #w for write
# f.write("x Doramming")

with open("filehandlingpart2.txt" ,"r") as f:
    print(f.read())