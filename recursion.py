# def repeat(n):
#     print(n)
#     if n<0:
#         return
#     repeat(n-1)
# repeat(10)

lst = ['mango','banana','papaya']
indexList = len(lst)-1

def list_items(indexList):
    if indexList<0:
        return
    print(lst[indexList])
    list_items(indexList-1)
    

list_items(indexList)