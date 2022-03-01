# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 03:52:30 2022

@author: fredb
"""

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right = Paddle((350,0))
left = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right.go_up, "Up")
screen.onkey(right.go_down, "Down")
screen.onkey(left.go_up, "w")
screen.onkey(left.go_down, "s")
game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bouncex()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()