# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 21:05:34 2025

@author: Lorand
"""
import random

print("Bun venit la ghicitoarea mea de cuvinte")


words = ["caine", "autobuz", "automat", "programare", "copil",
        "rezonabil", "python", "vandut"]

word = random.choice(words)

print("Ghiceste caracterele din cuvant")

guesses = ''
turns = 10

while turns > 0:
    
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
            
        else:
            print("_", end=" ")
            failed += 1
            
    if failed == 0:
        print("\nAi castigat")
        print("\nCuvantul este:", word)
        break
    print()
    guess = input("Ghiceste litera:")
    
    guesses += guess
    
    if guess not in word:
        
        turns -= 1
        print("Gresit")
        print("Mai ai", + turns, "incercari")
        
        if turns == 0:
            print("Ai pierdut")
