from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # The size will be 10 x 10 pixels .
        self.shapesize(stretch_len = 0.5 , stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        # position of the food .
        self.refresh()
       

    def refresh(self):
        random_x = random.randint( -280 , 280)
        random_y = random.randint( -280 , 280)
        self.goto( random_x , random_y )
        
