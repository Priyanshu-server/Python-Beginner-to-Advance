try:
    num = int(input("Enter a Number : "))
except ValueError:
    print("Exception Error !!")
else:
    print("Else statement !!")
finally:
    print("I am Final Statement")