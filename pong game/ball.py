from turtle import Turtle
# import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        # Create a ball:
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move_ball(self):
        """ Move the ball to the right up corner"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x , new_y)

    def bounce_y(self):
        """ reverse the ball """
        self.y_move *= -1

    def bounce_x(self):
        "Change the direction of the ball , and increases speed of the ball ."
        self.x_move *= -1
        # 0.9 is about the acceleration of the ball .
        self.move_speed *= 0.8

    def reset_position(self):
        """ Return the ball to (0 , 0) , and reaset the speed of the ball"""
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()