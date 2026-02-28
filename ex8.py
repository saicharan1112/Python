import random
num=random.sample(range(1,100),20)
print(num)
small=None
large=None
for i in num:
    if small is None or small>i:
        small=i
print("small:",small)
for i in num:
    if large is None or large<i:
        large=i
print("large:",large)