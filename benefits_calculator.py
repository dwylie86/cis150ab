# David Wylie
# CIS150AB Spring 2025
# Benefits Calculator (benefits_calculator.py)

# Define test cases for employee tenure and weekly hours
# These lists represent various test cases for employee tenure (in days)
employee_tenure = [-5, 0, -3, 1, 32, 1, 25, 31, 32, 40, 1000]
employee_weekly_hours = [-10, 0, 25, -3, 170, 30, 20, 19, 30, 20, 19]


def benefits_checker(tenure, weekly_hours):
    """
    This function checks if the employee is eligible for benefits
    based on tenure and weekly hours.

    :param tenure: Employee's tenure in days
    :param weekly_hours: Employee's weekly working hours
    :return: A string indicating benefit eligibility
    """
    if tenure <= 0 or weekly_hours <= 0 or weekly_hours > 168:
        return "Invalid Input, must input positive integers" \
            " for tenure and weekly hours"
    elif tenure > 31 and weekly_hours >= 30:
        return "Eligible for full benefits"
    else:
        if tenure <= 31:
            return "Not eligible for benefits based on tenure"
        elif weekly_hours >= 20:
            return "Eligible for reduced benefits"
        else:
            return "Not eligible for benefits based on weekly hours"


def run_test_cases():
    """
    This function runs test cases for the benefits_checker function
    using predefined employee tenure and weekly hours.

    :return: None
    """
    print("Running test cases...\n"
          "-----------------------------------")

    for i in range(len(employee_tenure)):
        tenure = employee_tenure[i]
        weekly_hours = employee_weekly_hours[i]

        result = benefits_checker(tenure, weekly_hours)
        print(f"Test case {i + 1}:\nTenure = {tenure}, "
              f"Weekly Hours = {weekly_hours}\nResult: {result}\n"
              f"-----------------------------------")

    print("\nAll test cases completed.")


# Run the test cases
run_test_cases()
