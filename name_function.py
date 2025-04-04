# David Wylie
# CIS150AB Spring 2025
# Functions - Scenario 1 (name_function.py)

def name_function(str1, str2, num):
    """
    This function combines two strings and prints them
    a specified number of times.

    :param str1: String 1
    :param str2: String 2
    :param num: Number of times the combined strings should be printed

    :return: None, just outputs
    """
    # Check if the number is a positive integer
    if not isinstance(num, int) or num <= 0:
        raise ValueError("Invalid Input: must be a positive integer for 'num'")

    for i in range(num):
        print(str1, str2)


# Test the function with different inputs
test_cases = [
    ("David", "Wylie", 3),
    ("Karate", "Kid", 5),
    ("Test", "Zero", 0),
    ("Test", "Negative", -2),
    ("Test", "Type", "three")
]


def run_test_cases():
    """
    This function runs test cases for the name_function
    using predefined test cases.

    :return: None, just outputs
    """
    print("Running test cases...\n"
          "-----------------------------------")
    passed = 0
    failed = 0
    for i, (t1, t2, num) in enumerate(test_cases, 1):
        try:
            print(f"Test {i}: ({t1}, {t2}, {num})")
            name_function(t1, t2, num)
            passed += 1
            print("Passed\n")
        except ValueError as e:
            print(f" Failed: {e}\n")
            failed += 1
    print(f"**All test cases completed: {passed} passed, {failed} failed.**")


run_test_cases()
