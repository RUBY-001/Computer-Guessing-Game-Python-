#SAMPLE 2 only useful if user enter string instead of number

import random
comp = random.randint(1,100)
attemps = 0
try:
   while True:
        user = int(input("Guess the Number : "))
        attemps = attemps + 1
        
        if(user == comp):
           print(f"You guessed the right Number {comp}\nYour attemps were {attemps}")
           break
        elif(user>comp):
         print("LOWER IT PLZ")

        elif(user<comp):
           print("HIGHER IT PLZ")

except ValueError as v:
   print("Value error u only need to guess Numbers")
