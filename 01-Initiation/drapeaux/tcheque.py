from turtle import *


speed(0)

up()
goto(-100, -100)
down()

begin_fill()
color('blue')
goto(0,0)
goto(-100,100)
end_fill()

up()
goto(-100, -100)
down()
begin_fill()
color('red')
goto(0,0)
goto(200,0)
goto(200,-100)
end_fill()


up()
goto(-100, -100)
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


