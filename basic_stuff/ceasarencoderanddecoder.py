# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 02:27:22 2022

@author: fredb
"""

alphabet_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
instructions = input("Type 'encode' or 'decode': \n")
text = input("Type your word: \n").lower()
shift = int(input("Type your shifting number: \n"))
shift = shift % 26

def encode(text, shift):
    cipher = ""
    for i in text:
        pos = alphabet_letters.index(i)
        newpos = pos + shift
        newlet = alphabet_letters[newpos]
        cipher += newlet
    print(f"Encoded text is {cipher}")
    
def decode(text, shift):
    plain = ""
    for i in text:
        pos = alphabet_letters.index(i)
        newpos = pos - shift
        plain += alphabet_letters[newpos]
    print(f"Decoded text is {plain}")
    
if instructions == "encode":
    encode(text, shift)
elif instructions == "decode":
    decode(text, shift)
else:
    print("Very funny")