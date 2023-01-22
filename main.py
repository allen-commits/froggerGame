import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(fun=player.move_up, key="Up")
car = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()

    if car.collide(player):
        game_is_on = False
    else:
        car.move_cars()

    if player.finish_line():
        player.reset_position()
        car.increase_speed()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()

screen.exitonclick()
