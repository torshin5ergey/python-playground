# Magic 8 Ball

from random import choice
from time import sleep

ANSWERS = ("It's certain",
           	"It's decidely so",
           	"Without a doubt",
           	"Yes definitely",
           	"You may rely on it",
           	"As I see it, yes",
           	"Most likely",
           	"Outlook good",
           	"Signs point to yes",
           	"Yes",
           	"Reply hazy, try again",
            "Ask again later", 
            "Better not tell you now", 
            "Cannot predict now", 
            "Concentrate and ask again", 
            "Don't count on it", 
            "My reply is no", 
            "My sources say no", 
            "Outlook not so good", 
            "Very doubtful")

# Check if the user input is empty
def user_input(message):
      while True:
            user = input(message).strip()
            if user:
                  return user

# Printing animation
def animation(duration):
      FRAMES = ("⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧")
      for _ in range(duration):
            for i in FRAMES:
                  print(f"The Magic 8 Ball is thinking... {i}", end="", flush=True)
                  print("\r", end="", flush=True)
                  sleep(.125)


print("\nHello, World! I'm the Magic 8 Ball, The Fortune Teller.\n"
      "And I know the answer to any question you have.")

name = user_input("What is your name?\n")
print(f"Hello, {name}.")

while True: # The main loop
      question = user_input("Write your question: ")
      animation(2) # animation for 2 seconds
      print(choice(ANSWERS) + " "*30)
      if input("\nDo you want to ask another question? (y/n): ").lower() != 'y':
            break
      print()
    
print("Come back if you have any questions!")