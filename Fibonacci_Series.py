def fab(n):
    if n<=1:
        return n

    return fab(n-1)+fab(n-2)



length = int(input("Enter length of series : "))
for i in range(length):
    print(fab(i))