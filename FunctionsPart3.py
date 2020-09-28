#using functions as an argument of another function
'''
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def diff_sum_and_sub(return_value_of_sum,return_value_of_sub):
    return return_value_of_sum-return_value_of_sub


print(diff_sum_and_sub(add(3,4),sub(5,4)))'''




def diff_sum_and_sub(a,b):
    def add(a,b):
        return a+b

    def sub(a,b):
        return a-b
    addition = add(a,b)
    subtraction = sub(a,b)
    return addition-subtraction

print(diff_sum_and_sub(5,4))