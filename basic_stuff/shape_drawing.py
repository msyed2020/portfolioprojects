# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:24:11 2022

@author: fredb
"""

from turtle import Turtle, Screen
import random

arrow = Turtle()

color_arr = ["blue", "red", "green", "yellow"]

def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        arrow.forward(100)
        arrow.right(angle)
        
for n in range(3,11):
    arrow.color(random.choice(color_arr))
    draw_shape(n)
    

screen = Screen()
screen.exitonclick()
