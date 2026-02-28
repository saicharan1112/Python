import random
for i in range(20):
    num=random.sample(range(1,100),20)
print(num)
print("average is:",sum(num)/len(num))
large=0
second_large=0
small=100
second_small=100
for i in num:
    if i>large:
        second_large=large
        large=i
    elif second_large<i<large:
        second_large=i
for i in num:
    if i<small:
      second_small=small
      small=i
    elif second_small>i>small:
        second_small=i
print("largest is:",large)
print("second large is:",second_large)
print("smallest is:",small)
print("second small is:",second_small)
even=0
for i in range(len(num)):
    if i%2==0:
        even+=1
print("even numbers count:",even)     
