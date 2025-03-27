from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

screen.setup(width=800, height=600)
screen.title("Pong Game")

paddle = Paddle((350, 0))

def go_up():
    paddle.go_up()

def go_down():
    paddle.go_down()

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_on = True

while game_on:
    screen.update()

screen.exitonclick()