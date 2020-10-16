# def add(a,b,*args):
#     print(args)0
# add(1,23,32,4343,543)


# def info(**kwargs):
#     print(kwargs)

# info(name = "xDoramming",age = 3000,favLang = "Python")


def info(a,b,*args,**kwargs):
    print(a,b,args,kwargs,sep = "\n")

info(2,3,4,5,6,7,name = "xDoramming",age = 3000)