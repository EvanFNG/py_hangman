import os
import random

# Clear console function
clear = lambda: os.system('cls')

# Word bank.
with open("words.txt", 'r') as f:
    words = f.read().splitlines()

# Difficulty / word length choice.
def getDiffChoice():

    difficulty_options = {'Easy': 4, 'Medium': 8, 'Hard': 9}
    valid_choice = False

    while not valid_choice:
        clear()
        diff_choice = input('Choose easy, medium or hard difficulty.').title()
        if diff_choice in difficulty_options.keys():
            valid_choice = True

    return {diff_choice: difficulty_options[diff_choice]}

def getWordChoice():

    diff_choice = getDiffChoice()
    
    if 'Easy' in diff_choice.keys():
        while True:
            word_choice = random.choice(words)
            if len(word_choice) <= diff_choice['Easy']:
                break

    elif 'Medium' in diff_choice.keys():
        while True:
            word_choice = random.choice(words)
            if len(word_choice) > diff_choice['Medium'] and len(word_choice) <= diff_choice['Medium']:
                break

    else:
        while True:
            word_choice = random.choice(words)
            if len(word_choice) >= diff_choice['Hard']:
                break

    return word_choice

 
