# David Wylie
# CIS150AB Spring 2025
# Functions - Scenario 2 (compensation_function.py)

def compensation_function(comp1, comp2):
    """
    Compare two compensation packages and return the difference.

    :param comp1: tuples in the format (salary, benefits, bonus)
    :param comp2: tuples in the format (salary, benefits, bonus)

    :return: None, just outputs any increases in salary, benefits, and bonus
    """
    # Check if the input is valid
    if len(comp1) != 3 or len(comp2) != 3:
        raise ValueError(
            "Invalid Input: compensation packages must be tuples of length 3"
        )
    if (
        not all(isinstance(i, (int, float)) for i in comp1)
        or not all(isinstance(i, (int, float)) for i in comp2)
    ):
        raise ValueError(
            "Invalid Input: compensation packages must contain numbers only"
        )
    if any(i < 0 for i in comp1 + comp2):
        raise ValueError(
            "Invalid Input: compensation packages must not "
            "contain negative values"
        )

    salary_increase = max(0, comp2[0] - comp1[0])
    benefits_increase = max(0, comp2[1] - comp1[1])
    bonus_payable = max(0, comp2[2] - comp1[2])
    print(
        f"""Salary Increase: ${salary_increase:,.2f}
Benefits Increase: ${benefits_increase:,.2f}
Bonus Payable: ${bonus_payable:,.2f}"""
    )


def error_check(prompt):
    """
    Prompt the user for a non-negative float.
    Repeats until valid input is entered.

    param: User Input
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Value cannot be negative. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """
    Get user input for two compensation packages and compare them.
    Keeps prompting until valid, non-negative input is provided.
    """
    print("Enter previous compensation details:")
    salary1 = error_check("Previous Salary: ")
    benefits1 = error_check("Previous Benefits: ")
    bonus1 = error_check("Previous Bonus: ")

    print("\nEnter new compensation details:")
    salary2 = error_check("New Salary: ")
    benefits2 = error_check("New Benefits: ")
    bonus2 = error_check("New Bonus: ")

    comp1 = (salary1, benefits1, bonus1)
    comp2 = (salary2, benefits2, bonus2)

    print("\nComparison Results:")
    compensation_function(comp1, comp2)


# Test the function with different inputs
# expected to include both passes and intentional failures
test_cases_comp1 = [
    (0, 0, 0),
    (95000, 12000, 5000),
    (65000.00, 12000.50, 5000.65),
    ("One-Hundred", "TwoFlower", -150),
    (0, 0, 0),
    (3000, 4150.00, 2300.50),
    (1, 2),
    (1, 2, 3),
    (-1, 2, 3),
    (1, 2, 3)
]
test_cases_comp2 = [
    (0, 0, 0),
    (95000, 12000, 5000),
    (85000.00, 10000.50, 10000.65),
    (100, 240, -150),
    (100, 200, 300),
    ("Test", "Type", "three"),
    (1, 2, 3),
    (1, 2),
    (1, 2, 3),
    (-1, 2, 3)
]


def run_test_cases():
    """
    This function runs test cases for the compensation_function
    using predefined test cases.

    :return: None, just outputs
    """
    print("Running test cases...\n"
          "-----------------------------------")
    passed = 0
    failed = 0
    for i, (comp1, comp2) in enumerate(
        zip(test_cases_comp1, test_cases_comp2), 1
    ):
        try:
            print(f"Test {i}: comp1 = {comp1}, comp2 = {comp2}")
            print("Program Output:")
            compensation_function(comp1, comp2)
            passed += 1
            print("Passed\n")
        except ValueError as e:
            print(f"Failed: {e}\n")
            failed += 1
    print(
        f"**All test cases completed: {passed} passed, {failed} failed. "
        f"(Note: Some failures expected)**"
        )


# Run test cases by default. Uncomment main() to run with user input instead.
if __name__ == "__main__":
    run_test_cases()
    # main()
