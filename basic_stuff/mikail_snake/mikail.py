# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:37:05 2022

@author: fredb
"""
from turtle import Turtle
#import time

START_POS = [(0,0),(-20,0),(-40,0)]
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Mikail:
    def __init__(self):
        self.segments = []
        self.create_mikail()
        self.head = self.segments[0]
        
    def create_mikail(self):
        for pos in START_POS:
            self.add_segment(pos)
    
    def add_segment(self, pos):
        new_seg = Turtle("square")
        new_seg.color("green")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(DIST)
        
    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)
    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)
    def left(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)
    def right(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        