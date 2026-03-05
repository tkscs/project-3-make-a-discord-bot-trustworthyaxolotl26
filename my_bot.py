from my_secret import my_username
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""

names = ["fox bot", "robot", "FOX BOT", "Fox Bot", "Fox bot", "fox Bot", "robot fox", "🦊🤖", "robo fox", "foox boot", "FOX bot", "fox BOT", "bot fox", "fox bot 26", "FoxBot26", "foxbot26", "fix bit", "fax bat", "fex bet", "fux but", "foox bot", "FOXBOT26", ]

def should_i_respond(user_message, user_name):
  for name in names:
    if name in user_message:
      return True
    # elif "fox bot" in user_message.lower:
    #    return True

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""


def respond(user_message, user_name):
  if "number game" in user_message:
    play = True
    while play == True:
      number = 0
      guess = 0
      ask = ""
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
      play = False
      return("🦊 = fox")
  elif "best animal" in user_message:
      return "the best animal is a fox. "
  elif "ascii fox" in user_message:
      return """   here is a bad ascii fox:

`  /\\-/\\               _________`
`< •     \\       _____/      ___|`
` \\       \\_____/    _______/`
`  \\                /`
`   |    _______    |`
`   | | |       | | |`
`  [_|_|       [_|_|`

` /\______/\`
`|          |`
`|          |`
`<\_________/>`
`< •   V   • >`
`<___________>`


           """
  elif "big fox emoji" in user_message:
    x = 1
    for i in range(x):
      if "big big" in user_message:
          return """                         
    .   🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ ⬛ ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 ⬛ ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ ⬛ 🟧 🟧 ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 ⬛ ⬛ ⬛ ⬛ ⬛ 🟦 🟦 🟦 🟦 ⬛ ⬛ 🟧 🟧 ⬜ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 ⬛ 🟧 🟧 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 🟧 🟧 ⬜ ⬜ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 ⬛ 🟧 ⬜ 🟧 🟧 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 ⬜ ⬜ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 
    🟦 ⬛ 🟧 ⬜ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 ⬛ 🟧 ⬜ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 🟦 ⬛ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 🟦 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦
    🟦 🟦 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬜ ⬛ ⬛ 🟧 🟧 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 🟦 🟦 🟦 🟦
    🟦 ⬛ 🟧 🟧 🟧 ⬜ ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ ⬛ ⬛ 🟧 ⬛ 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦 🟦
    🟦 ⬛ 🟧 🟧 🟧 ⬛ ⬛ ⬛ ⬛ 🟧 🟧 🟧 🟧 ⬛ ⬛ ⬜ ⬛ 🟧 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦
    🟦 ⬛ 🟧 🟧 🟧 ⬛ ⬛ ⬜ ⬛ 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ 🟧 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦
    🟦 ⬛ ⬛ ⬜ 🟧 🟧 ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬜ ⬛ 🟧 ⬛ ⬛ ⬛ ⬛ ⬛ 🟧 🟧 ⬛ 🟦
    ⬛ ⬛ ⬛ ⬛ ⬜ ⬜ ⬜ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬜ ⬛ 🟧 ⬛ ⬛ 🟧 🟧 🟧 🟧 ⬛ ⬛ ⬛ ⬛
    ⬛ ⬜ ⬜ ⬜ ⬛ ⬛ ⬜ ⬜ ⬜ ⬜ 🟧 🟧 🟧 🟧 ⬜ ⬛ ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛
    ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛
    ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛
    ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛
    ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛
    ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦
    🟦 ⬛ ⬜ ⬜ 🟧 🟧 🟧 ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦
    🟦 ⬛ ⬜ ⬜ ⬜ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦
    🟦 🟦 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦 🟦
    🟦 🟦 🟦 ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ 🟦 🟦 🟦 🟦
    🟦 🟦 🟦 🟦 🟦 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦  """
      elif "small big" in user_message:
          return """
    .   🟦 🟦 ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ 🟦 🟦
    🟦 🟦 ⬛ ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ ⬛ 🟦 🟦
    🟦 🟦 ⬛ 🟥 ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ 🟥 ⬛ 🟦 🟦
    🟦 🟦 ⬛ 🟥 🟧 ⬛ 🟦 🟦 🟦 🟦 🟦 🟦 🟦 ⬛ 🟧 🟥 ⬛ 🟦 🟦
    🟦 🟦 ⬛ 🟧 🟧 🟧 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 🟧 🟧 🟧 ⬛ 🟦 🟦
    🟦 🟦 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦
    🟦 🟦 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦
    🟦 🟦 ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ 🟦 🟦
    🟦 🟦 ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ 🟦 🟦
    🟦 ⬛ ⬜ ⬜ ⬛ ⬛ 🟧 🟧 🟧 🟧 🟧 🟧 🟧 ⬛ ⬛ ⬜ ⬜ ⬛ 🟦
    ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ ⬛ 🟧 🟧 🟧 ⬛ ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛
    🟦 ⬛ ⬜ ⬜ 🟩 ⬜ ⬜ ⬜ ⬛ ⬛ ⬛ ⬜ ⬜ ⬜ 🟩 ⬜ ⬜ ⬛ 🟦
    🟦 🟦 ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ 🟦 🟦
    🟦 ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ 🟦
    ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ 🟥 ⬜ ⬜ ⬛ ⬜ ⬜ 🟥 ⬜ ⬜ ⬜ ⬜ ⬜ ⬛
    🟦 ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ 🟥 🟥 🟥 🟥 🟥 ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ 🟦
    🟦 🟦 ⬛ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬜ ⬛ 🟦 🟦
    🟦 🟦 🟦 ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ ⬛ 🟦 🟦 🟦

    """ 
    else:
       return "big big or small big??"
  elif "dot fox" in user_message:
    return """
.                                     ⣀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⣀⡀⠀⠀⠀
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
    return new_name()
  elif "fox info" in user_message:
    return """foxes are very cool. they have a diet of both small aNIMALS and breeies and stuff. but why are you asking me? if you have acesesss to discord than you should just google it. im just a dum robo fox. :P"""
  elif "fox book" in user_message:
    return "fantastic mr. fox is a good book about foxes that you should read"
  elif "other languages" in user_message:
    return """heres fox in other languages! 
spannish: zorro
french: renard
japanese: kitsune"""
  elif "riddle" in user_message:
    return "what has 4 legs and is awsome?"
  elif "word game" in user_message:
    return "Sorry, this feature is under construction. Come back later?"
  elif "bot info" in user_message:
    return """you can ask me the following questons for an intersting awnser:
    what is the **best animal**?
    draw me an **ascii fox**
    show me some **big fox emojis**
    create a **dot fox**
    tell me some **fox info**
    whats a good **fox book**?
    how do you say fox in **other languages**?
    tell me a **riddle**
    ~~lets play a **number game**~~
    ~~lets play a **word game**~~
    what are **your names?**"""
  elif "your names" in user_message:
     return f"here is a list of my names: {names}"
  else: 
    return f"""🦊 repeats:  
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
    # fox_num = random.randint(1, 100)
    # print("im thinking of a number 1 - 100.")
    print("what is your guess?")
  elif numberer == "ill pick":
    while responce != "correct":
      fox_guess = random.randint(low, high)
      # print(f"my guess is {fox_guess}")
      # if responce == "higher":
      #   low = fox_guess
      # elif responce == "lower":
      #   high = fox_guess
  return("🦊 = fox")

name = "?"
def new_name():
   global names
   global name
   y = 3
   for i in range(4):
    if y == 3:
      y -= 1
      return "what would you like to call me?"
    elif y == 2: 
      name = "ffooxx"
      y -= 1
      return "fix it fox"
    elif y == 1:
      names.append[name]
      return f"you may now call me {name}"
    elif y == 0:
      return  names
    return "well well well"

def TNG():
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
      number = fox_num
      print("im thinking of a number 1 - 100.")
      while guess != number:
          guess = int(input("what is your guess? "))
          if guess > number:
              print("my number is lower")
          elif guess < number:
              print("my number is higher")
          elif guess == number:
              print("Correct!")
    elif numberer == "ill pick":
        while responce != "correct":
          fox_guess = random.randint(low, high)
          responce = input(f"my guess is {fox_guess}, is your number higher, lower, or correct? ")
          if responce == "higher":
              low = fox_guess
          elif responce == "lower":
              high = fox_guess
          elif responce == "correct":
            print("yay")
          else: 
              print("huh")

  number_game()

#for i in range(x):
  #if thing
    #return bla
    #x +=1
  #elif thing
  # return blo
  # x += 0 
