from turtle import *


#we want to pain a house

#step 1: draw a square
width(3)
color("purple")

      
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
#end of squeare

#drawing a door



left(90)
forward(70)
color("red")
begin_fill()
left(90)
forward(100)

right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200, 200)
pendown()

        
color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


penup()
goto(40,120)
pendown()
color("blue")
begin_fill()
right(150)
forward(40)
right(90)
forward(40)       
right(90)
forward(40)
right(90)
forward(40)      
end_fill()



penup()
goto(120,120)
pendown()
color("blue")
begin_fill()
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()



exitonclick()