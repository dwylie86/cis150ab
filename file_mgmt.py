# David Wylie
# CIS150AB Spring 2025
# File Management Program (file_mgmt.py)

# A basic program that:
# 1) Prompts the user for a filename.
# 2) Then, create a file that generates ten random integers.
# The file that your program creates should be a .txt file
# Important: The numbers that are generated must be truly random
# (hint: built-in function)
import random


def rand_nums_tofile(file_name):
    """
    Generate ten random integers and write them to a file.
    :param filename: The name of the file to write to.
    :return: None, writes to the file.
    """
    with open(file_name, 'w') as file:
        for i in range(10):
            random_number = random.randint(1, 100)
            file.write(f"{random_number}\n")
    print(f"Random numbers written to {file_name}")


def main():
    """
    Main function to execute the program.
    :return: None
    """
    print("Welcome to the Random Number File Generator!")
    print("This program will create a file with ten random integers.")
    print("The numbers will be between 1 and 100.")

    file_name = input("Enter the filename (without extension): ") + ".txt"
    rand_nums_tofile(file_name)


if __name__ == "__main__":
    main()
