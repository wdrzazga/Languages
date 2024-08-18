import functions
from words import *

choices = {1: 'EN',
           2: 'PL',
           3: 'ES',
           4: 'RU'}



while True:
    functions.display_menu(['English', 'Polski', 'Español', 'Русский'])
    choice = int(input("Choose the number of your language: "))
    if choice in choices:
        lan = choices[choice]
        break
    else:
        print("\nInvalid choice\n")

name = input(age_question[lan])
if lan == 'RU':
    name = functions.latin_to_cyrillic(name)
greet(name, lan)
