# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 21:07:40 2022

@author: fredb
"""

# Blackjack, the game famously named after Spongebob's cousin

import random

def card_deal():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card
def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, opponent_score):
    if user_score == opponent_score:
        return "Draw"
    elif opponent_score == 0:
        return "You lose, opponent got Blackjack"
    elif user_score == 0:
        return "You win, you got Blackjack"
    elif user_score > 21:
        return "You went over, you lose"
    elif opponent_score > 21:
        return "Opponent went over, you win"
    elif user_score > opponent_score:
        return "You win"
    else:
        return "You lose"
user_cards = []
opponent_cards = []
game_over_baby = False
for _ in range(2):
    opponent_cards.append(card_deal())
    user_cards.append(card_deal())
while not game_over_baby:
    user_score = calculate(user_cards)
    opponent_score = calculate(opponent_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Opponent's first card: {opponent_cards[0]}")
    if user_score == 0 or opponent_score == 0 or user_score > 21:
        game_over_baby = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal == "y":
            user_cards.append(card_deal())
        else:
            game_over_baby = True
while opponent_score != 0 and opponent_score < 17:
    opponent_cards.append(card_deal())
    opponent_score = calculate(opponent_cards)
print(f"User Final hand: {user_cards}, final score: {user_score}")
print(f"Opponent Final hand: {opponent_cards}, final score: {opponent_score}")
print(compare(user_score, opponent_score))
