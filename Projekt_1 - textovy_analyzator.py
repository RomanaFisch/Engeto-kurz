
# Autor: Romana Fischer
# Email: romana.fisch@gmail.com
# Discord: romca_28945

import string
import sys
print("$ python projekt1.py")

# Registrovaní uživatelé
registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Oddělovač
separator = "-" * 40

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Funkce pro odstranění interpunkce
def odstranit_interpunkci(text):
    interpunkce = string.punctuation
    return ''.join([char for char in text if char not in interpunkce])

# Získání přihlašovacích údajů uživatele
user_name = input("Zadej své jméno: ").lower()  # Převedeme jméno na malá písmena pro srovnání
print("Username:", user_name)
password = input("Zadej své heslo: ")
print("Password:", password)

# Ověření, zda zadané jméno a heslo odpovídají registrovaným uživatelům
if registered_users.get(user_name) != password:
    print("Unregistered user, terminating the program...")  # Neregistrovaný uživatel, ukončujeme program
    sys.exit()

else:
    print(separator)
    print(f"Welcome to the app, {user_name}")  # Registrovaný uživatel, přivítání
    print("We have 3 texts to be analyzed.")
    print(separator)

# Výběr textu
while True:
    try:
        user_choice = int(input("Enter a number btw 1 and 3 to select: "))  # Uživatel zadá volbu textu
        if user_choice < 1 or user_choice > 3:
            print("Toto není správná volba, zkus to znovu.")
            continue
        text_choice = TEXTS[user_choice - 1]  # Vybereme text podle volby uživatele
        print(f"Enter a number btw 1 and 3 to select: {user_choice}")
        break  # Pokud je volba správná, pokračujeme
    except ValueError:
        print("Neplatný vstup, prosím zadej číslo mezi 1 a 3.")
        
print(separator)

# Čistíme text od interpunkce před analýzou
text_choice = odstranit_interpunkci(text_choice)

# Analyzování vybraného textu
words_number = len(text_choice.split())

# Inicializace počtů pro analýzu
word_titlecase = 0
word_uppercase = 0
word_lowercase = 0
numeric = 0
total_sum = 0

# Analýza textu
for word in text_choice.split():
    if word.istitle():
        word_titlecase += 1
    elif word.isupper():
        word_uppercase += 1
    elif word.islower():
        word_lowercase += 1
    elif word.isnumeric():
        numeric += 1
        total_sum += int(word)  # Součet čísel

# Výstup analýzy
print(f"There are {words_number} words in the selected text.")
print(f"There are {word_titlecase} titlecase words.")
print(f"There are {word_uppercase} uppercase words.")
print(f"There are {word_lowercase} lowercase words.")
print(f"There are {numeric} numeric strings.")
print(f"The sum of all the numbers is {total_sum}.")

# Četnost různých délek slov v textu
star = "*"
space = " "
length_count = {}

# Vytvoření slovníku s délkami slov
for word in text_choice.split():
    length = len(word)
    length_count[length] = length_count.get(length, 0) + 1

# Vytisknutí délky slov a jejich četnosti seřazených od nejmenší po největší délku
print(f"LEN | OCCURRENCES  | NR.")
print(separator)

# Seřazení délky slov od nejmenší po největší
sorted_lengths = sorted(length_count.items())  # Třídění podle délky slova (key)

# Maximální počet výskytů pro formátování
max_number = max(length_count.values())  

for length, count in sorted_lengths:
    how_many_spaces = max_number - count  # Počet mezer pro správné zarovnání
    print(f"{length:>3} | {star * count} {space * how_many_spaces} | {count:>2}")
    
    
    





