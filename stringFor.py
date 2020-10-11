name = "xDoramming"
age = 250
#1st method 
'''
intro = "i am %s and my age is  %i"%(name,age )
print(intro)

'''

#2nd method
'''
# intro = "i am {} and my age is {}".format(name,age)
# intro = "i am {first} and my age is {second}".format(first = name,second = age)
intro = " i am {1} and my age is {0}".format(name,age)
print(intro)
'''
#3rd method

intro = f"i am {name} and my age is {age}"
print(intro)