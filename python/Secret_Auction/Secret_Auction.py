import os

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')
        
from art import logo
print(logo)

bid_details = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
      bid_amount = bidding_record[bidder]
      if bid_amount > highest_bid:
          highest_bid = bid_amount
          winner = bidder
          
    print(f"The winner is {winner} with a bid of ${highest_bid}")
    
    

while not bidding_finished:

    name = input("What is your name?: ")
    bid = int(input("How much do you want to bid? $"))
    bid_details[name] = bid
    
    should_continue = input("Are there any bidders? Type 'yes' or 'no'")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bid_details)
    elif should_continue == "yes":
        clear()

    
    