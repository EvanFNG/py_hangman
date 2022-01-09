# Hangman Game
import random
import os
from string import ascii_lowercase

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
    guess_dict = {i: '_' for i in range(len(word_choice))}

    while wrong_guesses < 5 and not won:
        print(guess_dict.values())
        
        guess_string = ""

        for i in guess_dict.values():
            guess_string += i

        if guess_string == word_choice:
            won = True
            break

        guess = input('Enter a letter: ').lower()
        if len(guess) != 1 or guess not in ascii_lowercase:
            print('Invalid guess. Enter a single letter.')

        elif guess in letters_guessed:
            print(f"You've already guessed {guess}. Try again.")

        elif guess not in word_choice:
            wrong_guesses += 1
            print(f'Wrong. You have {5 - wrong_guesses} guesses remaining.\n')
            letters_guessed.append(guess)
            print(f'These are your guesses: {letters_guessed}\n')
            print(f"Here's how many are correct: {guess_dict.values()}\n")

        else:
            print('Correct!\n')
            indexes = []
            for index, letter in enumerate(word_choice):
                if letter == guess:
                    indexes.append(index)

            for i in indexes:
                guess_dict[i] = guess

    if wrong_guesses == 5:
        clear()
        print("You've been hanged. F")
    else:
        print(f"You won! the word was: {word_choice.title()}")

main()


