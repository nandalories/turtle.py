import turtle

turtle.speed(0)
turtle.bgcolor("black")
colors = ["red", "green", "blue", "yellow", "purple"]

for i in range(150):
    turtle.pencolor(colors[i%5])
    turtle.forward(i*3)
    turtle.right(144)

turtle.done()
