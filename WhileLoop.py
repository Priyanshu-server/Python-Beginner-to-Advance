i = 0

# while i<4:
#     print(i) 
#     i = i+1  #<---

'''
for i in range(4):
    print(i)
'''

items = ["ListItems"]
# print(items[-1])

while items[-1]!='exit':
    user_item = input('Enter your item : ')
    items.append(user_item)
items.pop()
print(items)