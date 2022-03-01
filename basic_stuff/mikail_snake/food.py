# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 19:34:15 2022

@author: fredb
"""
from turtle import Turtle
import random
color_arr = ["blue", "green", "red", "yellow", "purple"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        self.color(random.choice(color_arr))
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)