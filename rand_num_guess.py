#!/usr/bin/env python3
# Created By: Maeva Tchuenga
# Date: 09, 12 2026
# this program is to guess the correct value
# of the output between 0 and 9

import random

# Generate a secret random number between 0 and 9 (inclusive)
secret_number = random.randint(0, 9)
user_input = input("Enter a number between 0 and 9: ")

# Check if the input is an integer
guess = int(user_input)
if guess != int(user_input):
    print("Invalid input! Please enter an integer.")

# Check if the guess is within the range 0 to 9
if guess < 0 or guess > 9:
    print("Out of range! Please pick a number from 0 to 9.")
elif guess == secret_number:
    print(f"Correct! The number was {secret_number}.")

else:
    print("Wrong guess, try again!")
