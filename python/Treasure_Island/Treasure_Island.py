print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
choice1 = input('You\'re at a crossroad, where do you want to go? Left or Right?\n').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. What colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over.")
        elif choice3 == "yellow":
            print("You found the treasure, you win!")
        elif choice3 == "blue":
            print("You entered a trap. Game over.")
        else:
            print("You got attacked by a bear.")
    else:
        print("You got attacked by an angry trout. Game over.")
else:
    print("Game over.")
