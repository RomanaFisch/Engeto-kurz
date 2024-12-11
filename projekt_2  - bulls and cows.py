"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Romana Fischer
email: romana.fisch@gmail.com
discord: romca_28945
"""

import random
import time

# úvodní informace
separator = "-" * 49
print("Hi there!")
print(separator)
print("I`ve generated a random 4-digit number for you.\nLet`s play a bulls and cows game.")
print(separator)

# funkce pro generování náhodných 4 číslic - secret_number, nebude obsahovat na prvním místě 0 a žádné duplicity
def generating_secret_number():
    while True:
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        secret_number = ''.join(map(str, random.sample(numbers, 4)))
        if secret_number[0] != '0':
            return secret_number

secret_number = generating_secret_number()
print("Test:", secret_number) #pro testování, abych věděla, co je správné číslo

# funkce pro výpočet počtu "bulls" a "cows"
def calculate_bulls_and_cows(secret, guess):
    bulls = 0
    cows = 0

    for i in range(4):
        if secret[i] == guess[i]:
            bulls += 1

    secret_counts = [0] * 10  # Počty číslic v tajném čísle
    guess_counts = [0] * 10   # Počty číslic ve vstupním čísle

    for i in range(4):
        if secret[i] != guess[i]:  # Pouze číslice, které nejsou bulls
            secret_counts[int(secret[i])] += 1
            guess_counts[int(guess[i])] += 1

    for digit in range(10):
        cows += min(secret_counts[digit], guess_counts[digit])

    return bulls, cows

# hlavní část hry
start_time = time.time() 
attempts = 0  

print("Enter a number:")

while True:
    print(separator)  
    print(">>> ", end="")  
    player_guess = input()
    attempts += 1  

    if not player_guess.isdigit():
        print("Invalid input. Please enter only numeric characters.")
    elif len(player_guess) != 4:
        print("Invalid input. Please enter a 4-digit number.")
    elif player_guess[0] == '0':
        print("Invalid input. The number cannot start with 0.")
    elif len(set(player_guess)) != 4:
        print("Invalid input. The number cannot contain duplicate digits.")
    else:
        bulls, cows = calculate_bulls_and_cows(secret_number, player_guess)
        
        # Změna výstupu na jednotné číslo, pokud je počet 1
        bulls_text = "bull" if bulls == 1 else "bulls"
        cows_text = "cow" if cows == 1 else "cows"
        
        print(f"Result: {bulls} {bulls_text} and {cows} {cows_text}.")
        
        if bulls == 4:
            end_time = time.time()  
            elapsed_time = round(end_time - start_time, 2)
            print(f"Congratulations! You've guessed the number in {attempts} attempts and {elapsed_time} seconds.")
            break


        



        
