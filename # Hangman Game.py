# Hangman Game
import random
import os

# Clear console function
clear = lambda: os.system('cls')

def main():
    words = [
        'koala',
        'chameleon',
        'tiger',
        'elephant'
    ]

    word_choice = random.choice(words)
    wrong_guesses = 0
    won = False

    letters_guessed = []
    guess_arr = ['_' for i in word_choice]

    while wrong_guesses < 5 and not won:
        print(guess_arr)
        if '_' not in guess_arr:
            won = True

        guess = input('Enter a letter: ').lower()
        guess_string = ""

        for i in guess_arr:
            guess_string += i

        if guess in letters_guessed:
            print(f"You've already guessed {guess}. Try again.")

        elif guess not in word_choice:
            wrong_guesses += 1
            print(f'Wrong. You have {5 - wrong_guesses} guesses remaining.\n')
            letters_guessed.append(guess)
            print(f'These are your guesses: {letters_guessed}\n')
            print(f"Here's how many are correct: {guess_arr}\n")

        else:
            print('Correct!\n')
            indexes = []
            for index, letter in enumerate(word_choice):
                if letter == guess:
                    indexes.append(index)

            for index, value in enumerate(guess_arr):
                pass

        


    if wrong_guesses == 5:
        clear()
        print("You've been hanged. F")



# string = 'elephant'
# letter = 'e'
# indices = []

# for index, value in enumerate(string):
#     if value == letter:
#         indices.append(index)

word = 'elephant'
guess_dict = {i: '_' for i in range(len(word))}

letter = 'e'
indexes = []

for index, value in enumerate(word):
    if value == letter:
        indexes.append(index)

for i in indexes:
    guess_dict[i] = letter

print(guess_dict)

guess_string = ""

for i in guess_dict.values():
    if i == '_':
        continue
    else:
        guess_string += i

print(guess_string)