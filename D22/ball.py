from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)  # 20x20 size
        self.penup()
        self.reset_speed()
        self.reset_position()
        self.game_over = False

    def reset_speed(self):
        # Set initial speed to ensure it hits a paddle
        # Horizontal speed is always positive (towards paddles)
        self.x_move = 0.8
        # Vertical speed is random but limited to ensure it hits paddle
        self.y_move = random.randint(-1, 1) * 0.5
        self.move_speed = 0.05 

    def reset_position(self):
        self.goto(0, 0)
        self.reset_speed()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y) 

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self, paddle_y=None):
        self.x_move *= -1
        
        # If paddle_y is provided, adjust vertical angle based on where it hit
        if paddle_y is not None:
            # Calculate the relative position of the hit (top = 1, bottom = -1)
            relative_y = (self.ycor() - paddle_y) / 50  # 50 is half the paddle height
            # Adjust vertical speed based on where it hit
            self.y_move = relative_y * 2  # Scale the angle effect

    def check_game_over(self):
        # Check for top/bottom wall collisions
        if self.ycor() > 280 or self.ycor() < -280:
            self.game_over = True
            return True
        
        # Check for left/right wall collisions
        if self.xcor() > 380 or self.xcor() < -380:
            self.game_over = True
            return True
        
        return False

    def check_paddle_collision(self, paddle):
        # Check if ball is close to paddle horizontally
        if abs(self.xcor() - paddle.xcor()) < 20:
            # Check if ball is within paddle's vertical range
            if (self.ycor() < paddle.ycor() + 50) and (self.ycor() > paddle.ycor() - 50):
                return True
        return False

    def update(self, r_paddle, l_paddle):
        # Check for top/bottom wall collisions
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

        # Check for paddle collisions
        if self.check_paddle_collision(r_paddle):
            self.bounce_x(r_paddle.ycor())
        elif self.check_paddle_collision(l_paddle):
            self.bounce_x(l_paddle.ycor())

        # Check for game over
        if self.check_game_over():
            return