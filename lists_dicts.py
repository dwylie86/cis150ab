# David Wylie
# CIS150AB Spring 2025
# Lists and Dictionaries (list_dicts.py)

# Task 1:
# Create a list containing two lists:
# one with names of 3 people
# one with ages of 3 people
# (you can choose the names/ages)

def create_lists():
    """
    This function creates two lists: one with names and one with ages.

    :return: None, just prints the lists
    """
    names = ["Crery", "Pofffe", "Charlie XCX"]
    ages = [25, 30, 32]
    print("Task 1: Names and Ages Lists")
    print("-" * 30)
    print(f"Names List: {names}\nAges List: {ages}\n")


create_lists()

# # Task 2:
# Write a Python script to concatenate the following dictionary
# to create some kind of merged array of data:

# Note: It's more challenging than it would seem.
# remember, to handle the duplicate keys in the dictionaries


def merge_dicts():
    """
    This function merges multiple dictionaries into one.
    Creating a new dictionary using a nested approach to maintain keys

    :return: None, just prints the merged dictionary
    """
    australian_cities = {1: "Sydney", 2: "Brisbane"}
    new_zealand_cities = {1: "Auckland", 2: "Wellington", 3: "Christchurch"}
    arizona_cities = {1: "Mesa", 2: "Phoenix", 3: "Flagstaff"}

    merged_cities = {
        "Australia": australian_cities,
        "New Zealand": new_zealand_cities,
        "Arizona": arizona_cities
    }
    print("Task 2: Merged Cities Dictionary")
    print("-" * 32)
    for country, cities in merged_cities.items():
        print(f"{country}:")
        for key, city in cities.items():
            print(f"  {key}: {city}")


merge_dicts()


# Task 3:
# Write code that removes "Flagstaff"
# from the merged array that was created in Task 2

def remove_flagstaff():
    """
    This function removes "Flagstaff" kv pair from the merged dictionary.

    :return: None, just prints the updated dictionary
    """
    australian_cities = {1: "Sydney", 2: "Brisbane"}
    new_zealand_cities = {1: "Auckland", 2: "Wellington", 3: "Christchurch"}
    arizona_cities = {1: "Mesa", 2: "Phoenix", 3: "Flagstaff"}

    merged_cities = {
        "Australia": australian_cities,
        "New Zealand": new_zealand_cities,
        "Arizona": arizona_cities
    }

    merged_cities["Arizona"].pop(3, "Key not found")
    print("\nTask 3: No Flagstaff Merged Cities Dictionary")
    print("-" * 45)
    for country, cities in merged_cities.items():
        print(f"{country}:")
        for key, city in cities.items():
            print(f"  {key}: {city}")


remove_flagstaff()
