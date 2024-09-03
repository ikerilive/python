print("Welcome to the ride")
height = int(input("What is your height?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        print("You pay $5")
    elif age <= 18:
        print("You pay $7")
    else:
        print("You pay $12")

else:
    print("Sorry, you can not ride the rollercoaster")