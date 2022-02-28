# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 15:24:47 2022

@author: fredb
"""

# Actually this app is more like a free draw, but nonetheless it could be considered an etch a sketch

from turtle import Turtle, Screen
arrow = Turtle()
screen = Screen()

def move_forward():
    arrow.forward(10)
    
def move_backward():
    arrow.backward(10)
    
def left():
    newh = arrow.heading() + 10
    arrow.setheading(newh)
    
def right():
    newh = arrow.heading() - 10
    arrow.setheading(newh)

def clear():
    arrow.clear()
    arrow.penup()
    arrow.home()
    arrow.pendown()
    
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(left, "a")
screen.onkey(move_backward, "s")
screen.onkey(right, "d")
screen.onkey(clear, "c")
screen.exitonclick()