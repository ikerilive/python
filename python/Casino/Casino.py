MAX_LINES = 3


def deposit():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES > 0:
                break
            else:
                print("Enter rvalid number of lines.")
        else:
            print("Please enter a number.")

        return lines
    
def get_number_of_lines():


def main():
    balance = deposit()
    lines = get_number_of_lines
    print(balance lines)


main()