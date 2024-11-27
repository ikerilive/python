from art import logo
#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Multiply
def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    
}

def calculator():
    
    print(logo)

    num1 = float(input("What is the first number?: "))

    continue_calculation = True

    while continue_calculation:
        for symbol in operations:
            print(symbol)
            
        operation_symbol = input("Pick an operation from above: ")

        num2 = float(input("What is the second number?: "))

        calculation_funtion = operations[operation_symbol]

        answer = calculation_funtion(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        should_continue = input(f"Do you want to continue calculating with {answer}? Type 'y' for yes or 'n' for no: ")

        if should_continue == 'y':
                    num1 = answer
        else:
            continue_calculation = False
            print("Goodbye!")

calculator()