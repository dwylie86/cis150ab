# David Wylie
# CIS150AB Spring 2025
# Exceptions Program (exceptions.py)

# Modify the below code in any way you see fit,
# so that non-integer input is caught without causing the program to crash
# I find that while loops are a great way to maintain control over user input.
# This allowed me to focus on the try/except blocks for specific exceptions
# while not having to worry about the program crashing

def grade_input():
    """
    Prompts the user for a grade percent and returns it as an integer.
    :param: None
    :return: An integer representing the grade percent
    """
    valid_input = False
    while valid_input is False:
        grade_input = input(
            "Please enter your grade percent as a positve whole number: "
            )
        try:
            if grade_input == "":
                raise ValueError("Input cannot be empty.")
            elif not grade_input.isdigit():
                raise ValueError("Input must be a positive whole number.")
            percent_grade = int(grade_input)
            valid_input = True
        except ValueError as e:
            print(e)
    return percent_grade


def letter_grade(percent_grade):
    """
    Determines the letter grade based on the percent grade.
    :param percent_grade: an integer representing the grade percent
    :return: None
    """
    if percent_grade > 100:
        letter_grade = "A+ (EXTRA CREDIT)"
    elif percent_grade >= 90:
        letter_grade = "A"
    elif percent_grade >= 80:
        letter_grade = "B"
    elif percent_grade >= 70:
        letter_grade = "C"
    elif percent_grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    print(f"Letter Grade: {letter_grade}")


# Main program
percent_grade = grade_input()
letter_grade(percent_grade)
