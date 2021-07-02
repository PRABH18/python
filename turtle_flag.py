import turtle
turtle.pensize(2)
turtle.speed(10)
turtle.bgcolor('white')
turtle.up()
turtle.goto(-200,200)
turtle.down()
def flagbox():
    turtle.fd(300)
    turtle.right(90)
    turtle.fd(50)

def flagdownbox():
    turtle.left(90)
    turtle.fd(15)
    turtle.left(90)


turtle.color('black','orange')
turtle.begin_fill()

flagbox()
turtle.right(90)
flagbox()
turtle.end_fill()
turtle.bk(50)
turtle.right(90)
flagbox()
turtle.right(90)
flagbox()
turtle.bk(50)
turtle.color('black','green')
turtle.begin_fill()
turtle.right(90)

flagbox()
turtle.right(90)

flagbox()
turtle.end_fill()
turtle.right(90)
turtle.fd(150)
turtle.up()
turtle.goto(-55,100)
turtle.down()
turtle.color('blue')
turtle.circle(25)
turtle.left(90)
turtle.fd(25)
for i in range(25):
    turtle.color('blue')
    turtle.pensize(2)
    turtle.fd(25)
    turtle.bk(25)
    turtle.right(20)
turtle.up()
turtle.color('black','brown')
turtle.begin_fill()
turtle.goto(-200,200)



turtle.down()
turtle.right(40)
turtle.fd(450)
turtle.right(90)
turtle.fd(15)
turtle.right(90)
turtle.fd(450)
turtle.right(90)
turtle.fd(15)
turtle.end_fill()
turtle.right(90)
turtle.fd(450)
turtle.right(90)
turtle.fd(40)

flagdownbox()
turtle.fd(80)

flagdownbox()
turtle.fd(80)
turtle.left(90)
turtle.fd(15)
turtle.right(90)
turtle.fd(25)

flagdownbox()
turtle.fd(130)

flagdownbox()
turtle.fd(130)
turtle.left(90)
turtle.fd(15)
turtle.right(90)
turtle.fd(25)

flagdownbox()
turtle.fd(180)

flagdownbox()
turtle.fd(180)

turtle.done()