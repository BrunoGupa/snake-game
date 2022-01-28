import turtle
from turtle import Turtle
import random

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

color_list = [(232, 52, 111), (230, 227, 81), (237, 220, 2), (17, 112, 177), (6, 196, 119), (232, 120, 171),
              (147, 64, 112), (225, 148, 54), (176, 194, 6), (221, 163, 216), (5, 175, 226), (242, 83, 32),
              (100, 199, 154), (108, 174, 204), (6, 53, 182), (9, 138, 95), (127, 222, 209), (219, 60, 18),
              (2, 93, 101), (240, 171, 162), (62, 25, 55), (18, 45, 73), (138, 30, 84), (4, 101, 82), (96, 111, 183),
              (154, 207, 218)]


class Snake:
    def __init__(self):
        turtle.colormode(255)
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in range(3):
            self.add_segment(position)

    def add_segment(self, position, color_pred=None):
        body_piece = Turtle(shape="square")
        if not color_pred:
            body_piece.color(random.choice(color_list))
        else:
            body_piece.color(color_pred)
        body_piece.penup()
        if position in [0,1,2]:
            body_piece.goto(x=-20 + position * 20, y=0)
        else:
            body_piece.goto(position)
        self.segments.append(body_piece)

    def reset(self):
        # Disappear the snake from the screen
        for seg in self.segments:
            seg.goto(999,999)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self, new_color):
        self.add_segment(self.segments[-1].position(), new_color)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
