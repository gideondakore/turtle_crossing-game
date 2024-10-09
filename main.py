import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
car_lists = [car_manager]
scoreboard = Scoreboard()

def create_car():
    new_car = CarManager()
    car_lists.append(new_car)


screen.listen()
screen.onkey(fun=player.move, key="Up")

create_bool = [False, False, False, False, False, False, True]


def is_collision(c_arg, p_arg):
    car_x, car_y = c_arg.position()  # Get car's position
    player_x, player_y = p_arg.position()  # Get player's position

    # Calculate half-widths and half-heights
    car_half_width = 40 / 2  # car's width is 40 pixels
    car_half_height = 20 / 2  # car's height is 20 pixels
    player_half_size = 20 / 2  # player's width and height are both 20 pixels

    # Check for collision (bounding box)
    if (abs(car_x - player_x) < car_half_width + player_half_size) and \
            (abs(car_y - player_y) < car_half_height + player_half_size):
        return True  # Collision occurred
    return False  # No collision



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # car_radius = 20
    # player_radius = 10

    for car in car_lists:
        if player.increase_movement:
            car.increase_movement()
            create_bool.append(True)
            player.increment_changer()
            scoreboard.update_score()
        car_manager.move(car)
        # if car.distance(player) < (car_radius + player_radius):
        if is_collision(car, player):
            game_is_on = False
            scoreboard.game_over()
    random.shuffle(create_bool)
    if random.choice(create_bool):
        create_car()

screen.exitonclick()