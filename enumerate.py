lst = ["eat","program","sleep","repeat"]
'''
enu_var = list(enumerate(lst))
print(enu_var)
'''
for index,item in enumerate(lst):
    if index ==2:
        print()
    else:
        print(item)
