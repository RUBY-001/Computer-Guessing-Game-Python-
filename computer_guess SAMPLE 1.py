# SAMPLE 1  Straightforward approach to computer guessing a number between 1 and x where computer guesses
# randomly and user (us) provides feedback on whether the guess is too high, too low, or correctand
# we aslo provide x the argument to the function computer_guess(x) as a range for the computer to guess from 1 to x.
# The computer will keep guessing until it gets the correct number and will also count the number of attempts it took to guess correctly.

import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempts = 0
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
            
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        attempts = attempts + 1
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly! under {attempts} attempts!')

computer_guess(100)

