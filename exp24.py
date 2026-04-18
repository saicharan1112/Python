class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, n):
        if n < 10:
            cost = n * self.price
        elif n < 100:
            cost = n * self.price * 0.9
        else:
            cost = n * self.price * 0.8
        return cost

    def make_purchase(self, n):
        self.amount = self.amount - n

name = input("Enter product name:")
amount = int(input("Enter no. of items for that product in stock:"))
price = float(input("Enter price of regular product:"))

p = Product(name, amount, price)

items = int(input("Enter no. of items to buy:"))

cost = p.get_price(items)
print("Final costs:", int(cost))

p.make_purchase(items)
print("Remaining stock is :", p.amount)
