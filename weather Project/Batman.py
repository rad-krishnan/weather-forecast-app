# Spiral Flower


import turtle

tina = turtle.Turtle()
tina.speed(10)
tina.hideturtle()
background = turtle.Screen()

tina_background =input("What color should the background be? ")                  #User defining the BG COLOUR
tina_color =input("What color should Tina use to draw? ")                        #Pen Colour

background.bgcolor(tina_background)
tina.color(tina_color)                                                          #Co-ordinates for the spirals
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)
tina.left(45)
tina.forward(20)
tina.circle(40)

#Extra
#The process will recur if the user wants to draw another layer
tina.left(46)
tina.forward(20)
tina.circle(40)
tina.left(46)
tina.forward(20)
tina.circle(40)
tina.left(46)
tina.forward(20)
tina.circle(40)
tina.left(46)
tina.forward(20)
tina.circle(40)
tina.left(46)
tina.forward(20)
tina.circle(40)
tina.left(46)
tina.forward(20)
tina.circle(40)
tina.left(46)
tina.forward(20)
tina.circle(40)
tina.left(46)
tina.forward(20)
tina.circle(40)


##### SPIRAL FLOWER with MANY LAYERS

import turtle
import math
import random
wn = turtle.Screen()
wn.bgcolor('black')
A = turtle.Turtle()
A.speed(0)
A.color('white')
rotate=int(360)
def drawCircles(t,size):
    for i in range(10):
        t.circle(size)
        size=size-4
def drawSpecial(t,size,repeat):
  for i in range (repeat):
    drawCircles(t,size)
    t.right(360/repeat)
drawSpecial(A,100,10)
S = turtle.Turtle()
S.speed(0)
S.color('yellow')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-10
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(S,100,10)
David = turtle.Turtle()
David.speed(0)
David.color('blue')
rotate=int(80)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-5
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(David,100,10)
RK = turtle.Turtle()
RK.speed(0)
RK.color('orange')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-19
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(RK,100,10)
W = turtle.Turtle()
W.speed(0)
W.color('pink')
rotate=int(90)
def drawCircles(t,size):
    for i in range(4):
        t.circle(size)
        size=size-20
def drawSpecial(t,size,repeat):
    for i in range (repeat):
        drawCircles(t,size)
        t.right(360/repeat)
drawSpecial(W,100,10)



####### Bat LOGO

import turtle
import math

myPen = turtle.Turtle()
myPen.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")                                      #defining the window 
myPen.color("yellow")

zoom=20

myPen.left(90)
myPen.penup()
myPen.goto(-7*zoom,0)
myPen.pendown()

for xz in range(-7*zoom,-3*zoom,1):
  x=xz/zoom
  absx=math.fabs(x)
  y=1.5*math.sqrt((-math.fabs(absx-1))*math.fabs(3-absx)/((absx-1)*(3-absx)))*(1+math.fabs(absx-3)/(absx-3))*math.sqrt(1-(x/7)**2)+(4.5+0.75*(math.fabs(x-0.5)+math.fabs(x+0.5))-2.75*(math.fabs(x-0.75)+math.fabs(x+0.75)))*(1+math.fabs(1-absx)/(1-absx))
  myPen.goto(xz,y*zoom)

for xz in range(-3*zoom,-1*zoom-1,1):
  x=xz/zoom
  absx=math.fabs(x)
  y=(2.71052+1.5-0.5*absx-1.35526*math.sqrt(4-(absx-1)**2))*math.sqrt(math.fabs(absx-1)/(absx-1))
  myPen.goto(xz,y*zoom)
  
myPen.goto(-1*zoom,3*zoom)
myPen.goto(int(-0.5*zoom),int(2.2*zoom))
myPen.goto(int(0.5*zoom),int(2.2*zoom))
myPen.goto(1*zoom,3*zoom)

for xz in range(1*zoom+1,3*zoom+1,1):
  x=xz/zoom
  absx=math.fabs(x)
  y=(2.71052+1.5-0.5*absx-1.35526*math.sqrt(4-(absx-1)**2))*math.sqrt(math.fabs(absx-1)/(absx-1))
  myPen.goto(xz,y*zoom)

for xz in range(3*zoom+1,7*zoom+1,1):
  x=xz/zoom
  absx=math.fabs(x)
  y = 1.5*math.sqrt((-math.fabs(absx-1))*math.fabs(3-absx)/((absx-1)*(3-absx)))*(1+math.fabs(absx-3)/(absx-3))*math.sqrt(1-(x/7)**2)+(4.5+0.75*(math.fabs(x-0.5)+math.fabs(x+0.5))-2.75*(math.fabs(x-0.75)+math.fabs(x+0.75)))*(1+math.fabs(1-absx)/(1-absx))
  myPen.goto(xz,y*zoom)

for xz in range(7*zoom,4*zoom,-1):
  x=xz/zoom
  absx=math.fabs(x)
  y=(-3)*math.sqrt(1-(x/7)**2) * math.sqrt(math.fabs(absx-4)/(absx-4))
  myPen.goto(xz,y*zoom)

for xz in range(4*zoom,-4*zoom,-1):
  x=xz/zoom
  absx=math.fabs(x)
  y=math.fabs(x/2)-0.0913722*x**2-3+math.sqrt(1-(math.fabs(absx-2)-1)**2)
  myPen.goto(xz,y*zoom)

for xz in range(-4*zoom-1,-7*zoom-1,-1):
  x=xz/zoom
  absx=math.fabs(x)
  y =(-3)*math.sqrt(1-(x/7)**2) * math.sqrt(math.fabs(absx-4)/(absx-4))
  myPen.goto(xz,y*zoom)
  
myPen.penup()
myPen.goto(300,300)



####Iron Man


from turtle import Turtle, Screen 
from time import sleep

#Top 
piece1 = [ [0, -2, -3.5, -6.5, -8.5, -8.5, -8.0, -8.5, -7.5, -7.0, -2.0, 0],[0, 0, 7, 5.5, 4, -1, -4, -5.5, -6.5, -5.5, -7.0, -7.0] ]
###Middle piece
piece2 = [ [0, -2.0, -2.5, -5.0, -6.5, -8.8, -9.3, -9.3, -6.0, -5.5, -4.0, -3.2, 0], [-7.5, -7.5, -8.0, -8.3, -8.0, -6.0, -7.5, -8.0, -14.5, -16.5, -17.5, -16.5, -16.5] ]
###Bottom
piece3 = [ [0, -3.0, -4.0, -5.5, -6.0, -4.5, -3.0, -1.5, -1.0, 0], [-17.0, -17.0, -18.0, -17.0, -18.5, -20.0, -19.0, -19.0, -18.5, -18.5] ]

t=Turtle()
s=Screen()
t.hideturtle()
s.bgcolor("#ba161e")          #Dark red
s.setup(500, 600)
x_offset, y_offset = 0, 120
zoom_factor = 15
t.speed(2)

def draw_piece(piece):
    t.penup()
    t.goto(piece[0][0] * zoom_factor + x_offset, piece[1][0] * zoom_factor + y_offset)
    t.pendown()
    t.color('#fab104')   #Light Yellow
    t.begin_fill()
    for i in range(1, len(piece[0])):
        x, y = piece[0][i] * zoom_factor + x_offset, piece[1][i] * zoom_factor + y_offset
        t.goto(x, y)
    #color("#f19100")     
    for i in range(len(piece[0])-1, -1, -1):
        x, y = piece[0][i] * zoom_factor * -1 + x_offset, piece[1][i] * zoom_factor + y_offset
        t.goto(x, y)
    t.end_fill()
    

draw_piece(piece1)
draw_piece(piece2)
draw_piece(piece3)
sleep(4)



'''
#### Panda
# Import turtle 
import turtle 

# Creating an object(pen) 
pen = turtle.Turtle() 

 
def ring(col, rad): 

	# Set the fill 
	pen.fillcolor(col) 

	# Start filling the color 
	pen.begin_fill() 

	# Draw a circle 
	pen.circle(rad) 

	# Ending the filling of the color 
	pen.end_fill() 

##########################Main ######################### 

# pen.up		  => move turtle to air 
# pen.down		  => move turtle to ground 
# pen.setpos		  => move turtle to given position 
# ring(color, radius)     => draw a ring of specified color and radius 
 

### Draw ears 
# Draw first ear 
pen.up() 
pen.setpos(-35, 95) 
pen.down 
ring('black', 15) 

# Draw second ear 
pen.up() 
pen.setpos(35, 95) 
pen.down() 
ring('black', 15) 

###To Draw face  
pen.up() 
pen.setpos(0, 35) 
pen.down() 
ring('white', 40) 

### Draw eyes ##black  

# Draw first eye 
pen.up() 
pen.setpos(-18, 75) 
pen.down 
ring('black', 8) 

# Draw second eye 
pen.up() 
pen.setpos(18, 75) 
pen.down() 
ring('black', 8) 

### Draw eyes white 

#To Draw the first eye 
pen.up() 
pen.setpos(-18, 77) 
pen.down() 
ring('white', 4) 

# TO Draw the second eye 
pen.up() 
pen.setpos(18, 77) 
pen.down() 
ring('white', 4) 

#To Draw nose
pen.up() 
pen.setpos(0, 55) 
pen.down 
ring('black', 5) 

# Draw mouth  
pen.up() 
pen.setpos(0, 55) 
pen.down() 
pen.right(90) 
pen.circle(5, 180) 
pen.up() 
pen.setpos(0, 55) 
pen.down() 
pen.left(360) 
pen.circle(5, -180) 
pen.hideturtle() 
'''


