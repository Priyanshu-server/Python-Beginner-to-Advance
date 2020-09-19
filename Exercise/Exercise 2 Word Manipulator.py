user_string = input("Enter your String :: ")
output = ""

for letter in user_string:
    if letter in "aeiou":
        output = output+"P"

    else:
        output = output+letter

print(output)