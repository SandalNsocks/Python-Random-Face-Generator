import turtle
import random

myTurtle = turtle.Turtle()

def drawcircle(x,y,radius,colour,outcolour):
  turtle.shape("turtle")
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color(colour)
  turtle.circle(radius)
  turtle.end_fill()
  turtle.color(outcolour)
  turtle.circle(radius)



def drawrectangle(x,y):
  turtle.shape("turtle")
  turtle.forward(x)
  turtle.left(90)
  turtle.forward(y)
  turtle.left(90)
  turtle.forward(x)
  turtle.left(90)
  turtle.forward(y)
  turtle.left(90)
  


def drawtriangle(x,y,z,colour):
  turtle.shape("turtle")
  turtle.penup()
  turtle.goto(-x,y)
  turtle.pendown()
  turtle.begin_fill()
  turtle.color(colour)
  turtle.forward(z)
  turtle.left(120)
  turtle.forward(z)
  turtle.left(120)
  turtle.forward(z)
  turtle.left(120)
  turtle.end_fill()
  
  
def drawrectangle(x,y):
  turtle.shape("turtle")
  turtle.forward(x)
  turtle.left(90)
  turtle.forward(y)
  turtle.left(90)
  turtle.forward(x)
  turtle.left(90)
  turtle.forward(y)
  turtle.left(90)
  
def drawsemicircle(x,y,size,angle):
  turtle.shape("turtle")
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.right(90)
  turtle.circle(size,angle)
  turtle.left(90)
  
face = 100
openmouth = 30
triangle = 10
circle = 50
size = 20
semicircle = 30
colour = "yellow"
facecolour = "black"
openmouthcolour = "red"

def drawsurprisedface():
  drawcircle(0,0,face,colour,facecolour)
  drawcircle(face / 2,face * 1.3,10,facecolour,facecolour)
  drawcircle(face / -2,face * 1.3,10,facecolour,facecolour)
  drawtriangle((triangle * 0.5),face,triangle,facecolour)
  #drawsemicircle(-50,50,40,-180)
  drawcircle(0,30,openmouth,openmouthcolour,facecolour)
  
def drawsadface():
  drawcircle(0,0,face,colour,facecolour)
  drawcircle(face / 2,face * 1.3,10,facecolour,facecolour)
  drawcircle(face / -2,face * 1.3,10,facecolour,facecolour)
  drawtriangle((triangle * 0.5),face,triangle,facecolour)
  drawsemicircle(-40,50,40,-180)
  
def drawhappyface():
  drawcircle(0,0,face,colour,facecolour)
  drawcircle(face / 2,face * 1.3,10,facecolour,facecolour)
  drawcircle(face / -2,face * 1.3,10,facecolour,facecolour)
  drawtriangle((triangle * 0.5),face,triangle,facecolour)
  drawsemicircle(-40,70,40,180)
  
ran = random.randint(1,3)
print(ran)
  
if ran == 1: 
  drawsurprisedface()

if ran == 2:
  drawhappyface()
  
if ran == 3:
  drawsadface()
