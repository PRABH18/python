from turtle import *
t=Turtle()
w=Screen()
w.title("mouse work")
t.pencolor("green")
t.shape("triangle")
t.speed(-90)
def paint(x,y):
    t.ondrag(None)
    t.setheading(t.towards(x,y))
    t.goto(x,y)
    t.ondrag(paint)

def erase(x,y):
    t.clear()

def main():
    w.listen()
    t.ondrag(paint)
    done()
main()

