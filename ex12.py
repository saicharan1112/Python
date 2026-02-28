a=input("Enter a sentence:")
b=a.split()
c=set()
e=[]
print("after split:",b)
for i in range(len(b)):
    c.update(b[i])
    e.append(i)
n=dict(zip(e,c))
print(c)
print(" ".join(b))
