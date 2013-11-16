import time
import turtle
t =  turtle.Turtle()
screen  = turtle.Screen()
screen.title('this is a new attempt')

def a():
  t.circle(50)
  t.pu()
  t.fd(50)
  t.lt(90)
  t.pd()
  t.fd(50)


def b():
  t.circle(50)
  t.pu()
  t.bk(50)
  t.lt(90)
  t.pd()
  t.fd(200)

def c():
  t.circle(50, extent=-180)

def d():
  t.circle(50)
  t.pu()
  t.fd(50)
  t.lt(90)
  t.pd()
  t.fd(200)

def e():
  t.circle(50, extent=-270)
  t.lt(90)
  t.fd(100)

def f():
  t.lt(90)
  t.fd(150)
  t.circle(-50, extent=180)
  t.pu()
  t.fd(50)
  t.rt(90)
  t.fd(50)
  t.pd()
  t.fd(100)

def g():
  t.circle(50)
  t.pu()
  t.circle(50, extent=90)
  t.fd(50)
  t.rt(180)
  t.pd()
  t.fd(150)
  t.circle(-50, extent=180)

def h():
  t.lt(90)
  t.fd(200)
  t.pu()
  t.bk(150)
  t.rt(90)
  t.pd()
  t.circle(-50, extent=90)
  t.fd(50)

def i(): 
  t.lt(90)
  t.fd(100)
  t.pu()
  t.fd(50)
  t.pensize(6)
  t.pd()
  t.fd(1)
  t.pensize(1)

def j():
  t.pu()
  t.bk(100)
  t.rt(90)
  t.pd()
  t.circle(50, extent=180)
  t.fd(100)
  t.pu()
  t.fd(50)
  t.pensize(6)
  t.pd()
  t.fd(1)
  t.pensize(1)

def k():
  t.lt(90)
  t.fd(200)
  t.pu()
  t.bk(150)
  t.rt(45)
  t.pd()
  t.fd(70.7)
  t.pu()
  t.bk(70.7)
  t.rt(90)
  t.pd()
  t.fd(70.7)

def l():
  t.lt(90)
  t.fd(200)

def m():
  t.lt(90)
  t.fd(100)
  t.pu
  t.bk(100)
  t.pd()
  t.circle(-50, extent=180)
  t.rt(180)
  t.circle(-50, extent=180)

def n():
  t.lt(90)
  t.fd(100)
  t.pu
  t.bk(100)
  t.pd()
  t.circle(-50, extent=180)

def o():
  t.circle(50)

def p():
  t.circle(50)
  t.pu()
  t.bk(50)
  t.rt(90)
  t.bk(50)
  t.pd()
  t.fd(200)

def q():
  t.circle(50)
  t.pu()
  t.fd(50)
  t.rt(90)
  t.bk(50)
  t.pd()
  t.fd(200)

def r():
  t.lt(90)
  t.fd(100)
  t.pu()
  t.bk(100)
  t.pd()
  t.circle(-50, 90)

def s():
  t.pu()
  t.fd(50)
  t.lt(90)
  t.fd(50)
  t.pd()
  t.circle(25, extent=270)
  t.circle(-25, extent=270)

def let_t():
  t.lt(90)
  t.fd(200)
  t.pu()
  t.bk(100)
  t.rt(90)
  t.bk(50)
  t.pd()
  t.fd(100)

def u():
  t.pu()
  t.fd(50)
  t.lt(90)
  t.pd()
  t.fd(100)
  t.circle(50, extent=-180)

def v():
  t.lt(60)
  t.fd(100)
  t.pu()
  t.bk(100)
  t.lt(60)
  t.pd()
  t.fd(100)

def w():
  t.lt(120)
  t.fd(100)
  t.pu()
  t.bk(100)
  t.rt(60)
  t.pd()
  t.fd(100)
  t.rt(120)
  t.fd(100)
  t.lt(120)
  t.fd(100)

def x():
  t.lt(60)
  t.fd(100)
  t.pu()
  t.bk(50)
  t.rt(120)
  t.bk(50)
  t.pd()
  t.fd(100)

def y():
  t.lt(120)
  t.fd(100)
  t.pu()
  t.bk(100)
  t.lt(120)
  t.bk(100)
  t.fd(200)

def z():
  t.fd(50)
  t.pu()
  t.bk(50)
  t.lt(60)
  t.pd()
  t.fd(100)
  t.lt(120)
  t.fd(50)
  
while True:
  a()
  time.sleep(2)
  break
