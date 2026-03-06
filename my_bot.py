from my_secret import my_username
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""

names = ["robot", "robot fox", "🦊🤖", "robo fox", "foox boot", "bot fox", "fox bot 26", "fix bit", "fax bat", "fex bet", "fux but", "foox bot", "🦊🤖26", "foxbot", "FoxBot", "🦊 🤖", ":fox: :robot:", ":fox::robot:", ]

def should_i_respond(user_message, user_name):
  for name in names:
    if name in user_message:
      return True
    elif "fox bot" in user_message.lower():
       return True
    elif "foxbot26" in user_message.lower():
       return True

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""

def respond(user_message, user_name):
  if "number game" in user_message.lower():
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
  elif "best animal" in user_message.lower():
      return "the best animal is a fox. "
  elif "ascii fox" in user_message.lower():
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
  elif "big fox emoji" in user_message.lower():
    x = 1
    for i in range(x):
      if "big big" in user_message.lower():
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
      elif "small big" in user_message.lower():
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
  elif "dot fox" in user_message.lower():
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
  elif "rename" in user_message.lower():
    return new_name()
  elif "fox info" in user_message.lower():
    return """foxes are very cool. they have a diet of both small aNIMALS and breeies and stuff. but why are you asking me? if you have acesesss to discord than you should just google it. im just a dum robo fox. :P"""
  elif "fox book" in user_message.lower():
    return "fantastic mr. fox is a good book about foxes that you should read"
  elif "other languages" in user_message.lower():
    return """heres fox in other languages! 
spannish: zorro
french: renard
japanese: kitsune"""
  elif "riddle" in user_message.lower():
    return "what has 4 legs and is awsome?"
  elif "word game" in user_message.lower():
    return "Sorry, this feature is under construction. Come back later?"
  elif "bot info" in user_message.lower():
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
    what are **your names**?"""
  elif "your names" in user_message.lower():
     return f"I respond to any form of 'foxbot' and 'foxbot26', but I also respond to: {names}"
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


def new_name():
   global names
   i = 4
   name = "?fox? ?bot?"
   names.append(name)
   for i in range(4):
    i -= 1
    if i == 3:
      return "what would you like to call me?"
    elif i == 2: 
      name = "ffooxx"
      return f"adding {name}"
    elif i == 1:
      names.append(name)
      return f"you may now call me {name}"
    elif i == 0:
      return  names

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


#     words = input("what is your message: ")

# def alt_caps(original_string):
#     x = 1
#     new_string = ""
#     i = 0
#     for character in words:
#         if x > 0:
#             words.upper
#             character.upper
#             new_string += words[i]
#             i += 1
#             x -= 1
#         else:
#            # words.lower
#             new_string += character
#             i += 1
#             x += 1
#     #new_string += words.upper()
#     return new_string
# print(alt_caps(words))

