# SAMPLE 3 with function and user can set the range of guessing number by passing the value in function

import random
def guess(x):
     comp = random.randint(1,x)
     attemps = 0
     while True:
         user = int(input(f"Guess the Number Btw 1 to {x}: "))
         attemps = attemps + 1
         
         if(user == comp):
           print(f"You guessed the right Number {comp}\nYour attemps were {attemps}")
           break

         elif(user>comp):
          print("LOWER IT PLZ")

         elif(user<comp):
          print("HIGHER IT PLZ")

guess(30)
