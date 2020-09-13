from turtle import *
speed(0)

up()
goto(-150,-150)
down()

begin_fill()
color('green')
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()

begin_fill()
color('yellow')
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()


begin_fill()
color('red')
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()


# etoile
up()
goto(25,-30)

down()
begin_fill()
color('green')
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)
right(144)
forward(50)


end_fill()


#bordure
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


