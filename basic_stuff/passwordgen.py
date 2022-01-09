# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 02:18:56 2021

@author: fredb
"""

# password generator

import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','^','&','*','(',')','+']

print("Welcome to Password Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

letlist = []
letcount = 0
for letter in letters:
    while (letcount < nr_letters):
        usedlet = random.choice(letters)
        letlist.append(usedlet)
        letcount += 1
#print(''.join(letlist))

symlist = []
symcount = 0
for lsymbol in symbols:
    while (symcount < nr_symbols):
        usedsym = random.choice(symbols)
        symlist.append(usedsym)
        symcount += 1
#print(''.join(symlist))

numlist = []
numcount = 0
for number in numbers:
    while (numcount < nr_numbers):
        usednum = random.choice(numbers)
        numlist.append(usednum)
        numcount += 1
#print(''.join(numlist))

# Inefficient and predictable solution
#letliststr = ''.join(letlist)
#symliststr = ''.join(symlist)
#numliststr = ''.join(numlist)

#output = str(letliststr + symliststr + numliststr)
#print(output)

# Practical and better solution

comb_list = letlist + symlist + numlist
#print(comb_list)
random.shuffle(comb_list)
output = ''.join(comb_list)
print(output)