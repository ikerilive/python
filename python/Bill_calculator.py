print("Welcome to the bill calculator")

total = float(input("Enter total amount\n"))

num_of_people = int(input("Enter number of people\n"))

tip_percentage = float(input("How many percent do you want to tip? Example: 10, 15 & 20\n"))

tip_amount = (tip_percentage / 100) * total

total_bill = total + tip_amount

each_person = (total_bill / num_of_people)

print(f"\nEach person pays: ${each_person:.2f}")