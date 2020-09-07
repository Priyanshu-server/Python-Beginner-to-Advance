age = int(input("Enter your age : "))
if 80>age>18:              #if condition is false then it will not execute the code in respected condition
    print("you can apply for job")
elif age>80:
    print("you are too old for a job")
else:               #agar 'if' conditional statement False hai
    print("you cannot apply for job")