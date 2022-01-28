import turtle
from turtle import Turtle
import random

color_list = [(232, 52, 111), (230, 227, 81), (237, 220, 2), (17, 112, 177), (6, 196, 119), (232, 120, 171),
              (147, 64, 112), (225, 148, 54), (176, 194, 6), (221, 163, 216), (5, 175, 226), (242, 83, 32),
              (100, 199, 154), (108, 174, 204), (6, 53, 182), (9, 138, 95), (127, 222, 209), (219, 60, 18),
              (2, 93, 101), (240, 171, 162), (62, 25, 55), (18, 45, 73), (138, 30, 84), (4, 101, 82), (96, 111, 183),
              (154, 207, 218)]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        turtle.colormode(255)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.new_color = random.choice(color_list)
        self.color(self.new_color)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.new_color = random.choice(color_list)
        self.color(self.new_color)
        self.goto(random_x, random_y)

