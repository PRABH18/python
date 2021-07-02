from turtle import *
t=Turtle()
w=Screen()
w.title("My Watch") #title
w.bgcolor("black")  #background color
t.hideturtle()   #turtle shape hide
t.shape("triangle")
t.speed(1)   #turtle speed
t.width(4)   #line width
t.color('red','white')    #outline red and fill color white
t.begin_fill()   #add with t.color
for i in range(4):
    t.forward(200)
    t.left(90)
    
    t.end_fill()

done()