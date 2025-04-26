# David Wylie
# CIS150AB Spring 2025
# Classes (travel_tracker.py)

# Imagine that you wanted to keep track of cities that you've visited...
# IMAGINE NO LONGER!
# With the travel tracker, your wildest dreams can come true!


class VisitedCity:
    def __init__(
            self, city_name, year_visited=2025, country="Not Entered",
            highlight="Not Entered", cuisine="Not Entered"
            ):
        """
        Constructor method to initialize the city object with default values.
        :param city_name: str, name of the city
        :param year_visited: int, year the city was visited, default is 2025
        :param country: str, country where the city is located
        :param highlight: str, a highlight of the city
        :param cuisine: str, a type of cuisine associated with the city
        """
        self.city_name = city_name
        self.year_visited = year_visited
        self.country = country
        self.highlight = highlight
        self.cuisine = cuisine

    def __str__(self):
        return (f"City: {self.city_name}\n"
                f"Year Visited: {self.year_visited}\n"
                f"Country: {self.country}\n"
                f"Highlight: {self.highlight}\n"
                f"Cuisine: {self.cuisine}\n"
                f"{'-' * 70}")


def get_user_input():
    """
    Function to get user input for city information.
    :return: list of city objects
    """
    travel_tracker = []

    while True:
        city_name = input("Enter the city name (or type 'x' to finish): ")
        if city_name.lower() == 'x':
            break

        # Make sure a city is entered
        if city_name.strip() == "":
            print("City name cannot be empty. Please enter a valid city name.")
            continue
        # Make sure the year is a number
        try:
            year_visited = int(input("Enter the year visited: "))
        except ValueError:
            print("Invalid year! Using current year instead.")
            year_visited = 2025

        country = input("Enter the country: ")
        highlight = input("Enter a highlight of the city: ")
        cuisine = input("Enter a type of cuisine associated with the city: ")

        city = VisitedCity(
            city_name, year_visited, country, highlight, cuisine
            )
        travel_tracker.append(city)

    return travel_tracker


def main():
    """
    Main function to run the program.
    """
    print("Welcome to the Travel Tracker!")
    print("-" * 70)

    cities = get_user_input()

    if not cities:
        print("No cities were entered.")
        print("-" * 70)
    else:
        print("\nCities Visited:")
        print("-" * 70)
        for city in cities:
            print(city)
    print("Thank you for using the Travel Tracker!")


if __name__ == "__main__":
    main()
