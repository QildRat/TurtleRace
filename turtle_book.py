import turtle as t
import random


class Appearance:

    def __init__(self, color, y):
        self.obj = t.Turtle()
        self.name = color
        self.color = self.obj.color(color)
        self.shape = self.obj.shape("turtle")
        self.obj.penup()
        self.obj.setposition(x=-200, y=y)

    def move_turtle(self):
        random_distance = random.randint(0, 10)
        self.obj.forward(random_distance)
