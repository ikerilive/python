from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Loop to keep the program running until the user chooses to exit
go_on = True
while go_on:

    # Ask for 'encode' or 'decode' input
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    
   
    while direction != "encode" and direction != "decode":
        direction = input("Invalid input. Please enter 'encode' or 'decode':\n")
    
    # Get the message and shift value from the user
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Caesar cipher function to encode/decode text
    def ceaser(start_text, shift_amount, cypher_direction):
        end_text = ""
        if cypher_direction == "decode":
            shift_amount *= -1  # Reverses the shift for decryption
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = (position + shift_amount) % 26
                end_text += alphabet[new_position]
            else:
                end_text += char  # Non-alphabet characters are unchanged
        print(f"The {cypher_direction}d text is {end_text}")

    # Call the Caesar cipher function with the user's inputs
    ceaser(start_text=text, shift_amount=shift, cypher_direction=direction)

    # Ask the user if they want to repeat or exit the program
    result = input("Type 'yes' to repeat or 'no' to exit.\n").lower()
    if result == "no":
        go_on = False  
        print("Goodbye!")
