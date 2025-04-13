from turtle import Screen ,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800 , height = 600)
screen.title("Pong")
screen.tracer(0)

# Create a paddle:
right_paddle = Paddle((350  , 0))
left_paddle = Paddle((-350 , 0))

# create a ball:
ball = Ball()

# Create a scoreboard
scoreboard = Scoreboard()

# move the paddles up , and down .
screen.listen()
screen.onkey(right_paddle.go_up , "Up" )
screen.onkey(right_paddle.go_down , "Down")

screen.onkey(left_paddle.go_up , "w")
screen.onkey(left_paddle.go_down , "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    # We move the ball to the up right corner by the loop .
    ball.move_ball()

    # Detect collision with wall :
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Need to bounce the ball
        ball.bounce_y()

    # Direct collision with the paddles:
    # The right_paddle is withh = 20 , and it's position is (350 , 0) .
    #  The ball is 20 x 20 , so the right boarder is 340 , the same with the small paddle .
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect right paddle miss the ball .
    # The width screen is 600 .
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    # Detect left paddle miss the ball .
    # The width screen is 600 .
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
    


screen.exitonclick()