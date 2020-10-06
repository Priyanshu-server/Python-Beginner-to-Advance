# x=10
# def price():
#     global x
#     x = 20
#     print(x)
# price()
# print(x)


x = 20 #Global

def func1():
    x = 30 #Local
    def func2():
        global x #Local
        x = 40
    func2()
    print(x)

func1()
print(x)