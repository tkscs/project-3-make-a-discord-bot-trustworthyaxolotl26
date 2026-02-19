from my_secret import my_username
import random

"""
**Do NOT change the name of this function.**

This function will be called every time anyone says anything on a channel where the bot lives.

* It returns `True` if the bot notices something it wants to repond to.
* You can have certain words or patterns in the messages trigger the bot.
* You can have the bot respond differently to different users
"""
def should_i_respond(user_message, user_name):
  if "fox bot" in user_message:
    return True
  elif "robot" in user_message:
    return True
  else:
    return False

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
    return """   /\/\                    ____
< •   \             __/       _]
  \      \_____/       __/
   \                       /
   |     ______     |
   | |  |            | |  |
 [_|_|           [_|_|
"""
  elif "show me" in user_message:
    return "not yet."
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
  return f"you may now call me {name}"