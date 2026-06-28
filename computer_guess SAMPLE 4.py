# SAMPLE 4 with function and user can set the range of guessing number

import random
def guess():
   comp = random.randint(1,20)
   attemps = 0
   user = 0
   while(user != comp):
      user = int(input("Guess the Number Btw 1 to 20: "))
      attemps = attemps + 1

      if(user>comp):
          print("LOWER IT PLZ")

      elif(user<comp):
          print("HIGHER IT PLZ")

   print(f"You guessed the right Number {comp}\nYour attemps were {attemps}")

guess()
