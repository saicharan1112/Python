def first_diff(s1, s2):
    n = min(len(s1), len(s2))
    for i in range(n):
        if s1[i] != s2[i]:
            return i
    if len(s1) != len(s2):
        return n
    return -1
s1 = input("Enter String1:")
s2 = input("Enter String2:")

result = first_diff(s1, s2)

if result == -1:
    print("Both are Identical")
    print(result)
else:
    print("Strings are different at first location is")
    print(result)
