first_digit = int(input("Enter your first digit : "))
second_digit = int(input("Enter your second digit : "))

print("1.+ve\n2.-ve\n3.multiply\n4.Divide")
operation = int(input("Enter your operation : "))
if operation ==1:
    print("Your result is ", first_digit+second_digit)
elif operation ==2:
    print("Your result is ", first_digit-second_digit)
elif operation ==3:
    print("Your result is ", first_digit*second_digit)
elif operation ==4:
    print("Your result is ", first_digit/second_digit)

else:
    print(" Wrong Input :: ")