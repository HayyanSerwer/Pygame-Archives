import math
import turtle
import random

root = turtle.Screen()
root.bgcolor('black')
height = 600
root.setup(width = 800, height = 600)
root.tracer(2)

pen2 = turtle.Turtle()
pen2.color("white")
pen2.speed(0)
pen2.penup()
pen2.hideturtle()
pen2.setposition(240, -220)


road = turtle.Turtle()
road.setposition(-0, -100)
road.penup()
road.shape('square')
road.color('grey')
road.shapesize(8,40)

road2 = turtle.Turtle()
road2.setposition(0, -30)
road2.penup()
road2.speed(0)
road2.shape('square')
road2.color('white')
road2.shapesize(1,50)

road3 = turtle.Turtle()
road3.setposition(0, -180)
road3.penup()
road3.speed(0)
road3.shape('square')
road3.color('white')
road3.shapesize(1,50)


SecondRoad = turtle.Turtle()
SecondRoad.setposition(-0, 150)
SecondRoad.penup()
SecondRoad.shape('square')
SecondRoad.color('grey')
SecondRoad.shapesize(8,40)

road2Object = turtle.Turtle()
road2Object.setposition(0, 220)
road2Object.penup()
road2Object.speed(0)
road2Object.shape('square')
road2Object.color('white')
road2Object.shapesize(1,50)

road3Object = turtle.Turtle()
road3Object.setposition(0, 80)
road3Object.penup()
road3Object.speed(0)
road3Object.shape('square')
road3Object.color('white')
road3Object.shapesize(1,50)

maxCars = 1
cars = []

for count in range(maxCars):
    cars.append(turtle.Turtle())
    cars[count].color("red")
    cars[count].shape("square")
    cars[count].shapesize(1,4)
    cars[count].penup()
    cars[count].speed(0)
    cars[count].setposition(random.randint(-600, -500), random.randint(-160, -100))
    
maxCars2 = 1
cars2 = []

for count in range(maxCars2):
    cars2.append(turtle.Turtle())
    cars2[count].color("red")
    cars2[count].shape("square")
    cars2[count].shapesize(1,4)
    cars2[count].penup()
    cars2[count].speed(0)
    cars2[count].setposition(random.randint(500,600), random.randint(-170, -110))

maxCarsSecond = 1
carsSecond = []

for count in range(maxCarsSecond):
    carsSecond.append(turtle.Turtle())
    carsSecond[count].color("red")
    carsSecond[count].shape("square")
    carsSecond[count].shapesize(1,4)
    carsSecond[count].penup()
    carsSecond[count].speed(0)
    carsSecond[count].setposition(random.randint(-600, -500), random.randint(80, 220))
    
maxCarsSecond2 = 1
carsSecond2 = []

for count in range(maxCarsSecond2):
    carsSecond2.append(turtle.Turtle())
    carsSecond2[count].color("red")
    carsSecond2[count].shape("square")
    carsSecond2[count].shapesize(1,4)
    carsSecond2[count].penup()
    carsSecond2[count].speed(0)
    carsSecond2[count].setposition(random.randint(500,600), random.randint(80, 220))

player = turtle.Turtle()
player.setposition(0, -250)
player.shape('square')
player.color('green')
player.shapesize(1,1)
player.speed(0)

def up():
    y = player.ycor()
    y += 20
    player.sety(y)

def down():
    y = player.ycor()
    y -= 20
    player.sety(y)

def right():
    x = player.xcor()
    x += 20
    player.setx(x)

def left():
    x = player.xcor()
    x -= 20
    player.setx(x)


def isCollision(t1, t2):
    d = math.sqrt(math.pow(player.xcor()-cars[count].xcor(), 2) + math.pow(player.ycor()-cars[count].ycor(),2))
    if d < 20:
        return True
    else:
        return False



turtle.listen()
turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(right, 'd')
turtle.onkey(left, 'a')
turtle.onkey(up, 'w')
turtle.onkey(down, 's')

player.penup()


while True:
    root.update()
    
    if player.ycor() > 800 or player.ycor() < -800:
        print('wad')

        
    for count in range(maxCars):
        cars[count].forward(1)
        
        if isCollision(player,cars[count]):
            cars[count].setposition(random.randint(-600, -500), random.randint(-160, -90))
            player.setposition(0, -250)

        if cars[count].xcor() > 400:
            cars[count].setposition(random.randint(-600, -500), random.randint(-160, -90))


    for count in range(maxCars2):
        cars2[count].forward(-1)

        if cars2[count].distance(player) < 20:
            cars2[count].setposition(random.randint(500,600), random.randint(-170, -110))
            player.setposition(0, -250)
            
            
        
        if cars2[count].xcor() < -400:
            cars2[count].setposition(random.randint(500,600), random.randint(-170, -110))


    for count in range(maxCarsSecond):
        carsSecond[count].forward(1)

        if carsSecond[count].distance(player) < 20:
            carsSecond[count].setposition(random.randint(-600, -500), random.randint(80, 220))
            player.setposition(0, -250)

        if carsSecond[count].xcor() > 400:
            carsSecond[count].setposition(random.randint(-600, -500), random.randint(80, 220))
            

    for count in range(maxCarsSecond2):
        carsSecond2[count].forward(-1)

        if carsSecond2[count].distance(player) < 20:
            carsSecond2[count].setposition(random.randint(500,600), random.randint(80, 220))
            player.setposition(0, -250)
            pen2.write("LOADING..", align="center", font=("Courier"))
            pen2.showturtle()
            
        if carsSecond2[count].xcor() < -400:
            carsSecond2[count].setposition(random.randint(500,600), random.randint(80, 220))





    


   

    

