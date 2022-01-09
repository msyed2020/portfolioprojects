# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 04:30:43 2022

@author: fredb
"""


bid = {}
finished = False
def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for i in bid_record:
        amount = bid_record[i]
        if int(amount) > int(highest_bid):
            highest_bid = amount
            winner = i
    print(f"The winner is {winner} with a bid of ${highest_bid}")
while not finished:
    name = input("What's your name?: ")
    price = input("How much will you bid?: ")
    bid[name] = price
    cont = input("Any others? Type 'yes' or 'no':")
    if cont == "no":
        finished = True
        find_highest_bidder(bid)
    elif cont != "yes":
        print("Very funny")