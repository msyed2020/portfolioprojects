# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 16:01:37 2022

@author: fredb
"""

from turtle import Turtle, Screen
from mikail import Mikail
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Mikail the Snake. Eat all the Sweettarts!")
screen.tracer(0)

mikail= Mikail()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(mikail.up,"Up")
screen.onkey(mikail.down,"Down")
screen.onkey(mikail.left,"Left")
screen.onkey(mikail.right,"Right")

game = True
while game:
    screen.update()
    time.sleep(0.1)
    mikail.move()
    if (mikail.head.distance(food) < 15):
        food.refresh()
        mikail.extend()
        scoreboard.increase_score()
        
    if mikail.head.xcor() > 280 or mikail.head.xcor() < -280 or mikail.head.ycor() > 280 or mikail.head.ycor() < -280:
        game = False
        scoreboard.game_over()
    
    for seg in mikail.segments:
        if seg == mikail.head:
            pass
        elif mikail.head.distance(seg) < 10:
            game = False
            scoreboard.game_over()
screen.exitonclick()