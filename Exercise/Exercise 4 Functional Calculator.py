def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def calcaulator():
    num1 = int(input("Enter your first digit : "))
    num2 = int(input("Enter your second digit : "))

    print("Enter your operation : \n1.Add\n2.Subtact\n3.Multiply\n4.Divide")
    operation = int(input("\nEnter your operation : "))
    if (operation == 1):
        print(add(num1,num2))

    elif(operation ==2):
        print(sub(num1,num2))

    elif(operation ==3):
        print(multiply(num1,num2))

    elif(operation ==4):
        print(divide(num1,num2))
    else:
        print("Enter a valid input --")

calcaulator()