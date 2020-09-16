num = int(input("Enter your number :: "))

for i in range(2,num):
    output = num%i
    if output == 0:
        print("Number is not prime")
        break;
else:
    print("Number is Prime")