# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 23:03:49 2021

@author: fredb
"""

# Hangman Game
import random

word_list = ['binarytree','linkedlist','hashtable']
chosen_word = random.choice(word_list)
display_list = ["_" for x in range(len(chosen_word))]

print("Solution is", chosen_word)
lives = 6
while ("_" in display_list and lives > 0):
    guess = input("Guess a letter. Must be lowercase\n").lower()
    for i in range(len(chosen_word)):
        
        new_letter = chosen_word[i]
        if (new_letter == guess):
            display_list[i] = new_letter
    if (guess not in chosen_word):
        lives -= 1
    print(display_list)
    print(lives)
if (lives == 0):
    print("You lost")
else:
    print("You won")
