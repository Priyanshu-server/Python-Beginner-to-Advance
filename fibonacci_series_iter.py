# 0 1 1 2 3 5 ...
rng = int(input("Enter your range for fib ser : "))
if rng == 0:
    print("Invalid input")
elif rng == 1:
    print(0)

else:
    n1,n2 = 0,1
    for i in range(rng):
        
        print(n1)
        nth = n1
        n1 = n2
        n2=  nth +n2