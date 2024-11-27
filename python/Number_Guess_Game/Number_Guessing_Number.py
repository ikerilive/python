import random
from art import logo
print(logo)

def set_difficulty():
    level = input("Choose difficulty level. Type 'Easy' or 'Hard' to begin: ").lower()
    if level == "easy":
        return 10
    elif level == "hard":
        return 5
    else:
        print("Inalid Input")
        return set_difficulty()
        
    
def play_game():        
    number_to_guess = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100.")

    attempts_remaining = set_difficulty()

    while attempts_remaining > 0:
        print(f"You have {attempts_remaining} to guess the number.")
        
        guess = int(input("Make a guess. Enter a number between 1 and 100: "))
        
        if guess > number_to_guess:
            print("Too high. Try again!")
        elif guess < number_to_guess:
            print("Too low. Try again")
        elif guess == number_to_guess:
            print(f"You guessed {number_to_guess}. You are correct! Bravo!!!")
            return
            
        attempts_remaining -= 1
        
    
    else:
        print(f"Sorry, you've run out of guesses. The correct number was {number_to_guess}.")
        
play_game()