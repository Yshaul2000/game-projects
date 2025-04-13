from turtle import Turtle

STARTING_POSITION = [( 0 , 0) , ( -20 , 0 ) , ( -40 , 0 )]
MOVE_STEP = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        # Snake is a collection of segments .
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)
    
    def add_segment(self , position):
         """ Get a position from the lise STARTING_POSITION , and create a new segment in position . """
         new_segment = Turtle( shape = "square")
         new_segment.color("white")
         new_segment.penup()
         # Add the new segment to same position of the last segment , but the move function move all sigments to the next segments position .
         new_segment.goto(position)
         self.segments.append(new_segment)

    def extend(self):
        """Extand the snake each time the snake eat food ."""
        #-1 is the last segment in the list .
        self.add_segment(self.segments[-1].position())
    

    def move(self):
        # The loop runing from the last to first .
        for seg_num in range(len(self.segments) - 1 , 0 , -1):
            new_x = self.segments[seg_num -1 ].xcor()
            new_y = self.segments[seg_num -1 ].ycor()
            self.segments[seg_num].goto( new_x , new_y )
        # The head is forward .
        self.head.forward(MOVE_STEP)
    
    def reset(self):
        """ Remove all the items in segments , and create a new segments ."""
        # Need to move the pld snake out of the screen size ( 600 x 600 )
        for seg in self.segments:
            seg.goto(1000 , 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


        
