from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

screen.setup(width=800, height=600)
screen.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

def r_paddle_go_up():
    r_paddle.go_up()

def r_paddle_go_down():
    r_paddle.go_down()

def l_paddle_go_up():
    l_paddle.go_up()

def l_paddle_go_down():
    l_paddle.go_down()

screen.listen()
screen.onkey(r_paddle_go_up, "Up")
screen.onkey(r_paddle_go_down, "Down")
screen.onkey(l_paddle_go_up, "w")
screen.onkey(l_paddle_go_down, "s")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()