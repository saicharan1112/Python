import turtle

# Create screen
screen = turtle.Screen()
screen.setup(800,600)
screen.title("Combined Turtle Diagrams")

t = turtle.Turtle()
t.speed(3)

# 1. Rectangle
t.penup()
t.goto(-300,100)
t.pendown()
for i in range(2):
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.left(90)

# 2. Circle
t.penup()
t.goto(150,100)
t.pendown()
t.circle(60)

# 3. Wheel (spokes)
t.penup()
t.goto(-200,-150)
t.pendown()
for i in range(12):
    t.forward(100)
    t.backward(100)
    t.left(30)

# 4. Flower pattern
colors = ["red","orange","yellow","green","blue","purple","cyan","pink"]

t.penup()
t.goto(150,-150)
t.pendown()

for i in range(36):
    t.pencolor(colors[i % len(colors)])
    t.circle(80)
    t.left(10)

turtle.done()
