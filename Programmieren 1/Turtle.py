import turtle
t=turtle.Turtle()
colors= ['red']
t.pen
turtle.bgcolor('black')
for x in range(1000):
    t.pencolor(colors[x%6])
    t.width(x/90+1)
    t.forward(x)
    t.left(10)