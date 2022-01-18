#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

actual_number = random.randint(1, 100)

if difficulty_level == "easy":
  attempts = 10
  print("You have 10 attempts remaining to guess the number.")
elif difficulty_level == "hard":
  attempts = 5
  print("You have 5 attempts remaining to guess the number.")

def guess():
  global attempts
  while attempts > 0:
    user_guess = input("Make a guess: ")
    user_guess_number = int(user_guess)
    if user_guess_number > actual_number:
      print("Too high.\nGuess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.")
    elif user_guess_number < actual_number:
      print("Too low.\nGuess again.")
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number.") 
    elif user_guess_number == actual_number:
      print(f"You got it! The answer was {actual_number}")
      attempts = -1

guess()
if attempts == 0:
  print("You've run out of guesses, you lose.")
elif attempts == -1:
  print("The End.")
