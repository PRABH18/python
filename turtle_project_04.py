import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.width(1)
t.speed(-110)
col=('blue','yellow','red','green','white')
for i in range(400):
    t.pencolor(col[i%2])
    t.forward(i*5)
    t.right(140)

turtle.done()