# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 11:52:47 2022

@author: fredb
"""
import random

attempt = 0
num = [i for i in range(1,101)]
inp = input("Guess a number between 1 and 100. Type 'easy' or hard'\n")
if (inp == "easy"):
    attempt = 10
elif (inp == "hard"):
    attempt = 5
else:
    print("Very funny")
chosen_num = random.choice(num)
# print(chosen_num) For testing purposes only
while (attempt > 0):
    guess_num = input("Guess the number\n")
    if (int(guess_num) == chosen_num):
        print("Congrats!")
        attempt = 0
    else:
        attempt -= 1