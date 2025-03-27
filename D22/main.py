from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

# Screen setup
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)

# Paddle size
screen.setup(width=800, height=600)
screen.title("Pong Game")

# Display paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Paddle movement
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Ball setup
ball = Ball()

game_on = True
while game_on:
    screen.update()
    ball.move()
    ball.update(r_paddle, l_paddle)

    # Check for game over (wall hit)
    if ball.check_game_over():
        game_on = False

# Game over display
screen.tracer(1)
game_over = Turtle()
game_over.hideturtle()
game_over.color("white")
game_over.penup()
game_over.goto(0, 0)
game_over.write("GAME OVER!", align="center", font=("Arial", 36, "normal"))

screen.exitonclick()