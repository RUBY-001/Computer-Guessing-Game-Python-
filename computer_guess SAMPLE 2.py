# SAMPLE 2 (friendly version) same but this time if say umber higher or lower it will move the ower and upper bounds accordingly
# and guess again until it gets the correct number. It will also count the number of attempts it took to guess correctly.


import random

low = 1
high = 100
a = 0

input("Think of a number between 1 and 100 👀\nPress Enter when you're ready...")

while True:
    comp = random.randint(low, high)  # Computer guesses a number in current range
    print(f"My guess is: {comp}")
    a = a + 1  # Count this guess as an attempt

    user = input("Is it (H)igher, (L)ower, or (C)orrect? ").strip().upper()

    if user == "C":
        print(f"I guessed your number {comp} 😎\nMy attempts were {a}")
        break
    elif user == "H":
        low = comp + 1  # You said your number is higher, so move the lower bound up
    elif user == "L":
        high = comp - 1  # You said your number is lower, so move the upper bound down
    else:
        print("Say 'H', 'L', or 'C' only bruh 😅")

