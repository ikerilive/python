import random
from art import logo, vs  
from game_data import data
def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
        
print(logo)       
score = 0
game_continue = True

def format_data(choice):
    choice_name = choice["name"]
    choice_descr = choice["description"]
    choice_country = choice["country"]

    return(f"{choice_name}, a {choice_descr} from {choice_country}")

def check_answer(guess, a_followers, b_followers):
    """Use user guess to check if they are correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

choice_b = random.choice(data)
            
while game_continue:

    choice_a = choice_b
    choice_b = random.choice(data)
    

    if choice_a == choice_b:
        choice_b = random.choice(data)
        
    print(f"Compare A: {format_data(choice_a)}")
    print(vs)
    print(f"Against B: {format_data(choice_b)}")

    guess = input("Who has more followers? 'A' or 'B'?: ").lower()

    a_follower_count = choice_a["follower_count"]
    b_follower_count = choice_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_continue = False
        print(f"You're wrong. Final score: {score}")

#check_answer()
