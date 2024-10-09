from ast import increment_lineno
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.resizemode("user")
        self.goto(STARTING_POSITION)
        self.increase_movement = False

    def move(self):
        self.goto(self.xcor(),  self.ycor() + MOVE_DISTANCE)
        if self.ycor() >= FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.increase_movement = True

    def increment_changer(self):
        if self.increase_movement:
            self.increase_movement = False




