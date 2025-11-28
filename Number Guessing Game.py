#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

def number_guessing_game():
    while True:  # main loop for multiple rounds
        number = random.randint(1, 20)
        attempts = 0

        print("\nWelcome to the number guessing game!")
        print("I have picked a number between 1 and 20. Can you guess it?")

        while True:
            # --- safe input handling ---
            user_input = input("Enter your guess: ")
            if not user_input.isdigit():
                print("Please enter a valid number.")
                continue

            guess = int(user_input)
            attempts += 1

            # --- comparison logic ---
            if guess < number:
                print("Too low. Try again.")
                if abs(guess - number) == 1:
                    print("You're very close!")
            elif guess > number:
                print("Too high. Try again.")
                if abs(guess - number) == 1:
                    print("You're very close!")
            else:
                print(f"Good job! You guessed it in {attempts} attempts.")
                break

        # --- play again prompt ---
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

number_guessing_game()


# In[ ]:




