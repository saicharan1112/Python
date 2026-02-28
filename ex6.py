import random
num=random.randint(0,10)
while True:
    guess = int(input("Guess a number between 1 and 10 until you get it right:"))
    if guess==num:
        print("Well guesed")
        break
