from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width = 600 , height = 600)
screen.bgcolor("black")
screen.title("Welcome to Snake Game:")
# The update of the screen will be manually .
screen.tracer(0)

# Create a new snake .
snake = Snake()

# Create a new food .
food = Food()

# Create a scoreboard .
scoreboard = Scoreboard()


#Control the snake .

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.right , "Right")
screen.onkey(snake.left , "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Check if the snake is eat the food .
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall (the screen size are 600 x 600 pixels) .
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # Detect collision with the tail .
    # Use in sliceing to get all the segments except the head .
    for segment in snake.segments[1:]:
         if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()