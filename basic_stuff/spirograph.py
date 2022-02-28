# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 21:40:37 2022

@author: fredb
"""

import turtle as t
import random

turt = t.Turtle()
t.colormode(255)

def rand_col():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    randcol = (r,g,b)
    return randcol

turt.speed("fastest")

def draw(size):
    for _ in range(360/size):
        turt.color(rand_col())
        turt.circle(100)
        turt.setheading(turt.heading() + size)

draw(5)

screen = t.Screen()
screen.exitonclick()
