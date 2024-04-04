def ascending(list):
    list.sort()
    return list
def descending(list):
    list.sort(reverse=True)
    return list
list = [5,6,3,9,2,1]
ascend = ascending(list)
print(list)
descend = descending(list)
print(list)
