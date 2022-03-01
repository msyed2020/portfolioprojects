# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 04:15:06 2022

@author: fredb
"""
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        x_co = self.xcor() + self.x_move
        y_co = self.ycor() + self.y_move
        self.goto(x_co, y_co)
        
    def bounce(self):
        self.y_move *= -1
    def bouncex(self):
        self.x_move *= -1
        self.move_speed * 0.9
        
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bouncex()