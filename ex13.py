a=[1,2,2,3,4,4,5,6,7,7]
for i in a:
  if a.count(i)>i:
    a.remove(i)
print(a)
