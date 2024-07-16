from turtle import Turtle, Screen


###################### challenge - etch-A-sketch ######################

screen = Screen()
t = Turtle()

t.speed("fastest")
def w():
  t.forward(40)

def s():
  t.backward(40)

def d():
  t.right(10)

def a():
  t.left(10)

def c():
  t.clear()
  t.penup()
  t.home()
  t.pendown()


screen.listen()
screen.onkey(w, 'w')
screen.onkey(s, 's')
screen.onkey(d, 'd')
screen.onkey(a, 'a')
screen.onkey(c, 'c')


screen.exitonclick()