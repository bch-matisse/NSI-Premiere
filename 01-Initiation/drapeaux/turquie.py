from turtle import *

speed(0)

up()
goto(-150,-150)
down()

begin_fill()
color('red')
forward(300)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)
left(90)
forward(300)
end_fill()


goto(-50,-100)
begin_fill()
color('white')
circle(50)
end_fill()
up()
goto(-40,-95)
begin_fill()
color('red')
circle(45)
end_fill()


# etoile
up()
goto(10,-40)
left(15)
down()
begin_fill()
color('white')
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
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


