def merge(list1, list2):
    result = list1 + list2
    result.sort()
    return result
a = [1, 4, 6]
b = [2, 3, 5]

print(merge(a, b))
