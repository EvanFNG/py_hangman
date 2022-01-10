# Hangman Game
import random
import os
from string import ascii_lowercase

os.chdir("C:/Users/Evan/Documents")

with open("words.txt", 'r') as f:
    words = f.read().splitlines()

# Clear console function
clear = lambda: os.system('cls')

def Game():
   
    difficulty_options = {'Easy': 4, 'Medium': 8, 'Hard': 9}

    valid_choice = False
    while not valid_choice:
        clear()
        diff_choice = input('Choose easy, medium or hard difficulty.').title()
        if diff_choice in difficulty_options.keys():
            valid_choice = True

    if diff_choice == 'Easy':
        while True:
            word_choice = random.choice(words)
            if len(word_choice) <= difficulty_options['Easy']:
                break

    elif diff_choice == 'Medium':
        while True:
            word_choice = random.choice(words)
            if len(word_choice) > difficulty_options['Easy'] and len(word_choice) <= difficulty_options['Medium']:
                break

    else:
        while True:
            word_choice = random.choice(words)
            if len(word_choice) >= 8:
                break

    wrong_guesses = 0
    won = False

    letters_guessed = []
    guess_dict = {i: '_' for i in range(len(word_choice))}

    while wrong_guesses < 5 and not won:
        print(f"{guess_dict.values()}\n")
        
        guess_string = ""

        for i in guess_dict.values():
            guess_string += i

        if guess_string == word_choice:
            won = True
            break

        guess = input('Enter a letter: ').lower()
        if len(guess) != 1 or guess not in ascii_lowercase:
            clear()
            print('Invalid guess. Enter a single letter.\n')
            print(guess_dict.values())

        elif guess in letters_guessed:
            clear()
            print(f"You've already guessed {guess}. Try again.\n")
            print(f"Already guessed: {letters_guessed}\n")

        elif guess not in word_choice:
            clear()
            wrong_guesses += 1
            print(f'Wrong. You have {5 - wrong_guesses} guesses remaining.\n')
            letters_guessed.append(guess)
            print(f'These are your guesses: {letters_guessed}\n')

        else:
            clear()
            print('Correct!\n')
            print(f"You have {5 - wrong_guesses} remaining.\n")
            letters_guessed.append(guess)
            print(letters_guessed)
            indexes = []
            for index, letter in enumerate(word_choice):
                if letter == guess:
                    indexes.append(index)

            for i in indexes:
                guess_dict[i] = guess

    if wrong_guesses == 5:
        clear()
        print(f"You've been hanged. F. The word was: {word_choice}")
    else:
        clear()
        print(f"You won! the word was: {word_choice.title()}")

if __name__ == "__main__":
    Game()



