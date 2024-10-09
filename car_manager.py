from pickle import NEWOBJ
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 20


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.create_car()
        self.increase_move = 0


    def create_car(self):
        self.color(random.choice(COLORS))
        self.goto(290 - self.xcor(), random.randint(-250, 250))

    def move(self, car):
        new_x = car.xcor() - STARTING_MOVE_DISTANCE
        car.goto(new_x-self.increase_move, car.ycor())

    def increase_movement(self):
        self.increase_move += MOVE_INCREMENT




