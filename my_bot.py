from my_secret import my_username
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""

names = ["fox bot", "robot", "FOX BOT", "Fox Bot", "Fox bot", "fox Bot", "robot fox", "🦊🤖"]

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
    number = 0
    guess = 0
    responce = ""
    low = 1
    high = 100
    numberer = "whould you like to pick a number or should i? "
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
    return("🦊 = fox")
  elif "best animal" in user_message:
      return "the best animal is a fox. "
  elif "ascii fox" in user_message:
      return """   here is a bad ascii fox

`  /\\-/\\               _________`
`< •     \\       _____/      ___|`
` \\       \\_____/    _______/`
`  \\                /`
`   |    _______    |`
`   | | |       | | |`
`  [_|_|       [_|_|`


           """
  elif "big fox emojis" in user_message:
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
🟦🟦🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦🟦🟦🟦🟦🟦  

🟦🟦⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟦🟦
🟦🟦⬛⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛⬛🟦🟦
🟦🟦⬛🟥⬛🟦🟦🟦🟦🟦🟦🟦🟦🟦⬛🟥⬛🟦🟦
🟦🟦⬛🟥🟧⬛🟦🟦🟦🟦🟦🟦🟦⬛🟧🟥⬛🟦🟦
🟦🟦⬛🟧🟧🟧⬛⬛⬛⬛⬛⬛⬛🟧🟧🟧⬛🟦🟦
🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦🟦
🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦🟦
🟦🟦⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛🟦🟦
🟦🟦⬛⬛🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧⬛⬛🟦🟦
🟦⬛⬜⬜⬛⬛🟧🟧🟧🟧🟧🟧🟧⬛⬛⬜⬜⬛🟦
⬛⬜⬜⬜⬜⬜⬛⬛🟧🟧🟧⬛⬛⬜⬜⬜⬜⬜⬛
🟦⬛⬜⬜🟩⬜⬜⬜⬛⬛⬛⬜⬜⬜🟩⬜⬜⬛🟦
🟦🟦⬛⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛🟦🟦
🟦⬛⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬛🟦
⬛⬜⬜⬜⬜⬜🟥⬜⬜⬛⬜⬜🟥⬜⬜⬜⬜⬜⬛
🟦⬛⬜⬜⬜⬜⬜🟥🟥🟥🟥🟥⬜⬜⬜⬜⬜⬛🟦
🟦🟦⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛🟦🟦
🟦🟦🟦⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛🟦🟦🟦


"""
  elif "dot fox" in user_message:
    return """
.                                     ⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
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
    return "fooxx" 
  elif "" in user_message:
    return """When a user says: fox bot tell me about foxes 
My bot will respond by: foxes 

When a user says: fox bot what is a good fox book? 
My bot will respond by: a good fox book is fantastic mr. fox

When a user says: fox bot lets play a word game 
My bot will respond by: ok how bout hangman? 
                        continue with game

When a user says: fox bot stump me/give me a riddle/puzzle
My bot will respond by:heres a riddle: [pick from multiple opotions]
                      option to show awnser and stuff
"""
  elif "other languages" in user_message:
    return """heres fox in other languages! 
                        spannish: zorro
                        french: renard
                        japanese: kitsune"""
  elif "riddle" in user_message:
    return "rid"
  elif "word game" in user_message:
    return "hangman?"
  else: 
    return f"""🦊 says 
    {user_message.replace("fox bot", user_name)}"""

number = 0
guess = 0
responce = ""
def number_game():
  low = 1
  high = 100
  global number
  global guess
  global responce
  numberer = "whould you like to pick a number or should i? "
  resopnce = numberer
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
  return("🦊 = fox")

def new_name():
  global names
  return "🦊 the 🦊"
  names.append[name]
  return f"you may now call me {name}"
