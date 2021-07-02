import turtle
import time
turtle.setup(600,600)
turtle.bgcolor('#08203D')
p=turtle.Turtle()
p.pencolor("DeepSkyBlue")
p.speed(0)
def spiral():
    for i in range(360):
        p.fd(i*5)
        p.right(121)

def spin(d):
    p.up()
    p.home()
    p.left(d*n)
    p.down()

try:
    n=0
    while True:
        turtle.tracer(0)
        p.clear()
        spin(-1)
        spiral()
        n+=1
        turtle.update()
        time.sleep(0.01)

except:
    print("exit")