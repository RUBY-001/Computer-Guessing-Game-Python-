# SAMPLE 1 imple straight forward code for guessing number game

import random
comp = random.randint(1,100)
attemps = 0
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
