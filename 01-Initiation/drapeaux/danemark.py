from turtle import *


speed(0)

up()
goto(-100, -100)
down()
begin_fill()
color('red')
goto(200,-100)
goto(200,100)
goto(-100,100)
goto(-100, -100)
end_fill()

up()
goto(-100, -20)
down()
begin_fill()
color('white')
goto(200,-20)
goto(200,20)
goto(-100,20)
goto(-100, -20)
end_fill()


up()
goto(-20, 200)
down()
begin_fill()
color('white')
goto(20, 200)
goto(20,-100)
goto(-20,-100)
goto(-20, 200)
end_fill()

# bordure
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


