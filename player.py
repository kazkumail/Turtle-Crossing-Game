from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

screen = Screen()


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape('turtle')
        self.speed('fastest')
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
