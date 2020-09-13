from turtle import *

speed(0)

up()
goto(-150,-150)
down()

begin_fill()
color('green')
forward(150)
left(90)
forward(200)
left(90)
forward(150)
left(90)
forward(200)
left(90)
forward(150)
end_fill()


goto(0,-100)
begin_fill()
color('red')
circle(50)
color('red')
circle(40)
end_fill()

up()
goto(-150,-150)
setheading(0)
down()
color("black")
width(6)
forward(300)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)

# ne pas oublier pour ne planter !
exitonclick()


