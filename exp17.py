def number_of_factors(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
            print(i)
    return count

num = int(input("Enter a number: "))
print("Number of factors:", number_of_factors(num))
