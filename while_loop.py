# David Wylie
# CIS150AB Spring 2025
# While Loop (while_loop.py)
# For Fun Challenge: Python can represent arbitrarily large integers,
# so I tested with 10^400 which Python accepted as valid input.
# However, we'll be long dead if this program ran to conclusion :)
# Ctrl + C and the Pause / Break button stops the program on my system

# Get the user input first, error checking to ensure acceptable loop range.
valid_input = False

while not valid_input:
    try:
        user_input = int(input("Enter a positive whole number: "))
        if user_input <= 0:
            print("The number must be positive.")
            continue
        valid_input = True
    except ValueError:
        print("That's not a valid number.")


def while_loop(user_input):
    """
    Takes user's input and runs a while loop that prints the numbers
    in the loop the start integer of 1 to the user's input.
    Parameters:
        user_input (int): User input variable

    Returns:
        None:
        The function prints the start integer and
        iteration values to the console
    """
    start_int = 1
    while start_int <= user_input:
        print(start_int)
        start_int += 1


# Then pass it to the function
while_loop(user_input)
