from turtle import Turtle

class Paddle(Turtle):

    def __init__(self  , position):
        super().__init__()
        # Create a paddle:
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize (stretch_len = 1 , stretch_wid = 5 )
        self.goto(position)

    def go_up(self):
        """ Move only the ycor up """
        new_y = self.ycor() + 20
        self.goto(self.xcor() , new_y)

    def go_down(self):
        """ Move only the ycor down """
        new_y = self.ycor() - 20
        self.goto(self.xcor() , new_y)

    