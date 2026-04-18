class Power:
    def pow(self, x, n):
        result = 1
        i = 0
        while i < n:
            result = result * x
            i += 1
        return result

p = Power()

x = int(input("Enter base value: "))
n = int(input("Enter power value: "))

print("Result:", p.pow(x, n))
