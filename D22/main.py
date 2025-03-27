from turtle import Screen
from paddle import Paddle

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
from ball import Ball


ball = Ball()

# In your game loop:
while game_on:
    ball.move()
    screen.update()

    # Check for top/bottom wall collisions
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Check for paddle collisions
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
game_on = True
while game_on:
    screen.update()

screen.exitonclick()