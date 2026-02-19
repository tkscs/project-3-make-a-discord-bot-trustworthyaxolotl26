from my_secret import my_username
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""

names = ["fox bot", "robot", "FOX BOT", "Fox Bot", "Fox bot", "fox Bot"]

def should_i_respond(user_message, user_name):
  for name in names:
    if name in user_message:
      return True
    
  # if "fox bot" in user_message:
  #   return True
  # elif "robot" in user_message:
  #   return True
  # elif "FOX BOT" in user_message:
  #   return True
  # elif "Fox Bot" in user_message:
  #   return True
  # elif "Fox bot" in user_message:
  #   return True
  # elif names in user_message:
  #   return True
  # else:
  #   return False

"""
**Do NOT change the name of this function.**

This function will be called every time the `should_i_respond` function returns `True`.

* This function returns a string.
* The bot will post the returned string on the channel where the original message was sent.
* You can have the bot respond differently to different messages and users
"""
def respond(user_message, user_name):
  if " number game" in user_message:
    number_game()
  elif "best animal" in user_message:
    return "the best animal is a fox. "
  elif "ascii fox" in user_message:
    return """   here is a bad ascii fox

  /\-/\              _________
< •    \       _____/      ___]
  \     \_____/      _____/
   \                /
   |    _______    |
   | | |       | | |
  [_|_|       [_|_|

           """
  elif "fox pic" in user_message:
    return """                
                                    ██                  
                                  ██  ██                
                                  ██    ██              
                                ██      ██              
      ████                ██████          ██        ████
      ██  ████        ████                ██      ██  ██
      ██      ████  ██░░░░░░  ░░  ░░      ██    ██    ██
      ████        ██░░░░░░░░░░░░░░  ░░  ██    ██    ████
      ██▒▒██        ██░░░░░░░░░░░░░░░░████  ██    ██▒▒██
      ██▒▒▒▒██        ██████████████████████    ██▒▒▒▒██
        ██▒▒▒▒██    ░░░░░░░░░░░░░░░░░░░░██    ██▒▒▒▒██  
        ██▒▒▒▒▒▒██  ░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒██  
          ██▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒██    
          ██▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░░░░░██▒▒▒▒▒▒██    
            ██▒▒▒▒██░░░░░░░░░░░░░░░░░░░░░░░░██▒▒▒▒██    
            ██▒▒██░░░░░░░░░░░░░░░░░░░░░░░░░░██▒▒██      
          ██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██        
        ██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
      ██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
    ██░░░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██      
  ██░░░░░░░░░░░░██░░██████░░░░░░░░░░░░░░██████░░██      
  ██░░░░░░░░░░░░██░░░░░░░░██░░░░░░░░░░██░░░░░░░░██      
  ██░░░░░░░░░░░░░░██░░░░░░░░██░░░░░░██░░░░░░░░██░░██    
██░░░░░░░░░░░░░░░░░░██░░░░░░░░    ░░  ░░░░░░██░░░░██    
██░░░░░░░░░░░░░░░░░░░░████░░    ████    ████░░░░░░░░██  
██░░░░░░░░░░██░░░░░░░░░░░░████        ██░░░░░░░░░░░░██  
  ██░░░░░░░░██░░░░░░░░██████████████████████░░░░░░░░██  
  ██░░░░░░░░░░████░░░░░░          ██          ░░░░░░██  
    ████████████████████████████████████████████████   

              
                                            
                   to see more foxes like this, go to https://textart.sh/topic/fox  """
  elif "dot fox" in user_message:
    return """⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀
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
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""
  elif "rename" in user_message:
    new_name()
  else: 
    return f"""I've been called!
    {user_message.replace("fox bot", user_name)}"""


def number_game():
  numberer = input("whould you like to pick a number or should i? ")
  if numberer == "you pick":
    fox_num = random.randint(1, 100)
    return "im thinking of a number 1 - 100"

def new_name():
  name = input("what shall my new name be?")
  names.append[name]
  return f"you may now call me {name}"