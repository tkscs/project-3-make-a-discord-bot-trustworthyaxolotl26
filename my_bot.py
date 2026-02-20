from my_secret import my_username
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""

names = ["fox bot", "robot", "FOX BOT", "Fox Bot", "Fox bot", "fox Bot", "robot fox"]

def should_i_respond(user_message, user_name):
  for name in names:
    if name in user_message:
      return True

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""

def respond(user_message, user_name):
  if "number game" in user_message:
    number_game()
  elif "best animal" in user_message:
    return "the best animal is a fox. "
  elif "ascii fox" in user_message:
    return """   here is a bad ascii fox

`  /\\-/\\              _________`
`< •      \\       _____/      ___]`
`\\       \\_____/      _____/`
` \\                /`
`   |    _______    |`
`   | | |       | | |`
`  [_|_|       [_|_|`

           """
  elif "big fox emoji" in user_message:
    return """                         
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦⬛⬛⬛🟦🟦🟦🟦🟦🟦🟦⬛⬛🟧🟧⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦⬛⬛⬛⬛⬛🟦🟦🟦🟦⬛⬛🟧🟧⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦⬛🟧🟧⬛⬛⬛⬛⬛⬛⬛🟧🟧⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦⬛🟧⬜🟧🟧⬛🟧🟧🟧🟧🟧🟧⬜⬜⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦⬛🟧⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦⬛🟧⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬜⬛⬛🟧🟧⬛⬛⬛⬛⬛⬛🟦🟦🟦🟦
🟦⬛🟧🟧🟧⬜⬛⬛🟧🟧🟧🟧🟧⬛⬛⬛⬛🟧⬛🟧🟧🟧🟧🟧⬛🟦🟦🟦
🟦⬛🟧🟧🟧⬛⬛⬛⬛🟧🟧🟧🟧⬛⬛⬜⬛🟧⬛🟧🟧🟧🟧🟧🟧⬛🟦🟦
🟦⬛🟧🟧🟧⬛⬛⬜⬛🟧🟧🟧🟧🟧⬛⬛🟧⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦
🟦⬛⬛⬜🟧🟧⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧⬜⬛🟧⬛⬛⬛⬛⬛🟧🟧⬛🟦
⬛⬛⬛⬛⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧⬜⬛🟧⬛⬛🟧🟧🟧🟧⬛⬛⬛⬛
⬛⬜⬜⬜⬛⬛⬜⬜⬜⬜🟧🟧🟧🟧⬜⬛⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛
⬛⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛
⬛⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛
⬛⬜⬜⬜⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛
⬛⬜⬜⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛
⬛⬜⬜⬜⬜⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦
🟦⬛⬜⬜🟧🟧🟧⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦
🟦⬛⬜⬜⬜🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦🟦
🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦🟦🟦
🟦🟦🟦⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛🟦🟦🟦🟦
🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦  """
  elif "dot fox" in user_message:
    return """
.
              ⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠙⠻⢶⣄⡀⠀⠀⠀⢀⣤⠶⠛⠛⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⣙⣿⣦⣤⣴⣿⣁⠀⠀⣸⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣡⣾⣿⣿⣿⣿⣿⣿⣿⣷⣌⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣷⣄⡈⢻⣿⡟⢁⣠⣾⣿⣦⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⠘⣿⠃⣿⣿⣿⣿⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠈⠛⣰⠿⣆⠛⠁⠀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣦⠀⠘⠛⠋⠀⣴⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣿⣿⡇⠀⠀⠀⢸⣿⣏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠀⠀⠀⠾⢿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⡿⠟⠋⣁⣠⣤⣤⡶⠶⠶⣤⣄⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⣿⣿⣮⣉⣉⣉⣤⣴⣶⣿⣿⣋⡥⠄⠀⠀⠀⠀⠉⢻⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣋⣁⣤⣀⣀⣤⣤⣤⣤⣄⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⠁⠀⠀⠀⠀⠈⠛⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
  elif "rename" in user_message:
    new_name()
  else: 
    return f"""I've been called!
    {user_message.replace("fox bot", user_name)}"""

number = 0
guess = 0
responce = ""
def number_game():
  low = 1
  high = 100
  global number
  global guess
  print("🦊 = fox")
  numberer = print("whould you like to pick a number or should i? ")
  if numberer == "you pick":
    fox_num = random.randint(1, 100)
    print("im thinking of a number 1 - 100.")
    print("what is your guess?")
  elif numberer == "ill pick":
    while responce != "correct":
      fox_guess = random.randint(low, high)
      print(f"my guess is {fox_guess}")
      if responce == "higher":
        low = fox_guess
      elif responce == "lower":
        high = fox_guess

def new_name():
  global names
  #//
  name = input("what shall my new name be?")
  #//
  names.append[name]
  return f"you may now call me {name}"
