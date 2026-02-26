
#ignore

import random

number = 0
guess = 0
responce = ""
def number_game():
  low = 1
  high = 100
  global number
  global guess
  global responce
  numberer = input("whould you like to pick a number or should i? ")
  if numberer == "you pick":
    fox_num = random.randint(1, 100)
    print("im thinking of a number 1 - 100.")
    print(input("what is your guess?"))
  elif numberer == "ill pick":
    while responce != "correct":
      fox_guess = random.randint(low, high)
      print(f"my guess is {fox_guess}")
      if responce == "higher":
        low = fox_guess
      elif responce == "lower":
        high = fox_guess