from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def collide(self, player):
        for car in self.all_cars:
            if car.distance(player) < 30:
                print("you done messed up aaron")
                return True

    def stop(self):
        for car in self.all_cars:
            car.backward(0)

    def collide_wall(self, player):
        for car in self.all_cars:
            if car.distance(player) < 30:
                return True

    def increase_speed(self):
        self.speed = self.speed + MOVE_INCREMENT

