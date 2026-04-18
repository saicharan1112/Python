def sum_digits(self,n):
    global sum
    sum=0
    for i in range(n):
        sum=sum+i
n=int(input("Enter a value: "))
sum_digits(n)
print(sum)