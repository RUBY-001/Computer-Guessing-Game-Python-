# SAMPLE 3 same as above but this time we will ask the user to provide the range for the computer to guess from 1 to x and also count the number of attempts it took to guess correctly.

import random

def cg():
   low = 1
   a = 0
   high = int(input("What should be the guessing Number range from 1 to ? : "))
   while True:
      comp = random.randint(low,high)
      user = input(f"Is the Number {comp}\nHigher(h)\nLower (l)\nCorrect (c)\n : ").lower()
      a = a+1

      if(user == "c"):
         print(f"Yess guessed the right Number in {a} Attempts")

      elif(user == "h"):
         low = comp + 1

      elif(user == "l"):
         high = comp - 1

      print("-------------------------------------------------------------------------------------------------------------------")

cg()
cg()
