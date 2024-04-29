import turtle
import time 


t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-250,0)
t.pendown()

def a():

  t.pd()
  t.left(60)
  t.forward(100)
  t.right(120)
  t.fd(50)
  t.rt(120)
  t.fd(50)
  t.bk(50)
  t.lt(120)
  t.fd(50)
  t.penup()
  t.lt(62)
  t.fd(10)
  t.pendown()

def d():
  t.lt(85)
  t.fd(85)
  t.lt(90)
  t.circle(42,-180)
  t.penup()
  t.lt(3)
  t.fd(60)
  t.pendown


def i():
  t.pd()

  t.lt(90)
  t.fd(85)

  t.pu()
  t.bk(85)
  t.rt(90)
  t.fd(20)
  t.pd()

def bigt():
  t.pu()
  t.fd(40)
  t.pd()
  t.lt(90)
  t.fd(85)
  t.lt(90)
  t.fd(50)
  t.bk(100)
  t.lt(90)
  t.pu()
  t.fd(85)
  t.lt(90)
  t.fd(20)
  t.pd()

def n():
  t.pd()
  t.lt(90)
  t.fd(85)
  t.rt(155)
  t.fd(90)
  t.lt(155)
  t.fd(83)
  t.bk(83)
  t.pu()
  t.rt(90)
  t.fd(10)
  t.pd()


def s():

  t.circle(22,155)
  t.circle(-25,185)
  t.pu()
  t.rt(60)
  t.fd(85)
  t.lt(90)
  t.fd(10)
  t.pd()


def h():

  t.lt(90)
  t.fd(85)

  t.bk(43)
  t.rt(90)
  t.fd(40)
  t.lt(90)
  t.fd(43)
  t.bk(85)

  t.pu()
  t.rt(90)
  t.fd(10)
  t.pd()

def z():

  t.pd()
  t.fd(100)
  t.bk(100)
  t.lt(45)
  t.fd(120)
  t.lt(135)
  t.fd(100)

  t.bk(100)
  t.lt(180)
  t.rt(135)
  t.fd(120)
  t.lt(135)
  t.pu()
  t.fd(120)
  t.pd


def k():
  t.pd()
  t.left(90)
  t.fd(85)
  t.bk(42)
  t.rt(35)
  t.fd(50)
  t.bk(50)
  t.rt(115)
  t.fd(50)
  t.pu()
  t.lt(65)
  t.fd(20)
  t.pd()

def m():
  t.pd()
  t.left(90)
  t.fd(85)
  t.rt(135)
  t.fd(40)
  t.lt(90)
  t.fd(40)
  t.rt(135)
  t.fd(85)
  t.pu()
  t.lt(90)
  t.fd(20)

def r():
  t.pd()
  t.left(90)
  t.fd(85)
  t.bk(40)
  t.rt(90)
  t.circle(20,180)
  t.lt(90)
  t.fd(40)
  t.lt(30)
  t.fd(50)
  t.pu()
  t.lt(60)
  t.fd(20)

def p():
  t.pd()
  t.left(90)
  t.fd(85)
  t.bk(40)
  t.rt(90)
  t.circle(20,180)
  t.lt(90)
  t.pu()
  t.lt(90)
  t.fd(30)

def y():
  t.pu()
  t.fd(10)
  t.pd()
  t.left(90)
  t.fd(45)
  t.left(35)
  t.fd(50)
  t.bk(50)
  t.right(70)
  t.fd(50)
  t.bk(50)
  t.left(215)
  t.fd(40)
  t.left(90)
  t.pu()
  t.fd(45)
  t.pd()







def curve():
    for i in range(200):

        # Defining step by step curve motion
        t.right(1)
        t.forward(1)

# Defining method to draw a full heart
def heart():

    # Set the fill color to red
    t.fillcolor('red')

    # Start filling the color
    t.begin_fill()

    # Draw the left line
    t.left(140)
    t.forward(113)

    # Draw the left curve
    curve()
    t.left(120)

    # Draw the right curve
    curve()

    # Draw the right line
    t.forward(112)

    # Ending the filling of the color
    t.end_fill()

# Defining method to write text
def txt(name):

    # Move turtle to air
    t.up()

    # Move turtle to a given position
    t.setpos(-48,-105)

    # Move the turtle to the ground
    t.down()

    # Set the text color to lightgreen
    t.color('lightgreen')

    # Write the specified text in 
    # specified font style and size
    t.write(f"{name}", font=(
      "Verdana", 12, "bold"))







def Me():
  a()
  a()
  d()
  i()
  bigt()

def Homie():
 
  time.sleep(2)
  a()
  y()
  m()
  a()
  n()
  t.pu()
  t.goto(0,-200)
  t.pd()
  heart()
  t.pu()
  while True:
    t.fd(1)




print(Homie())








