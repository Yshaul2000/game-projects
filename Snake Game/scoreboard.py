from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier" , 24 , "normal")

class Scoreboard (Turtle):

    def __init__(self):

        super().__init__()
        # The user score .
        self.score = 0
        # we read the higt_score value , and update his value in the data file .
        with open("data.txt") as data:
            # need to change the value from string to int to use him .
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto( 0 , 260 )
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}" , align = ALIGNMENT , font = FONT )

    def increase_score(self):
        self.score += 1
        # Write the new score on the screen
        self.update_score()

    def reset(self):
        """ Update the high score , and reset the score if gmae over ."""
        if self.score > self.high_score:
            self.high_score = self.score
            # update the value of high score to the data file in order to save it after we close the runnig of the code.
            with open("data.txt" , mode = "w") as data:
                data.write(f"{self.high_score}")
            self.score = 0
            self.update_score()

