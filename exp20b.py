def merge(list1, list2):
    result = []
    while list1 and list2:
        if list1[0] < list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    
    result += list1
    result += list2
    
    return result
a = [1, 4, 6]
b = [2, 3, 5]

print(merge(a, b))
