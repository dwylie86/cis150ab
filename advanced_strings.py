# David Wylie
# CIS150AB Spring 2025
# Advanced Strings (advanced_strings.py)

# Task 1:
# Print air_temperature 1 decimal point followed by F.
# Sample output with input: 101.193124
# 101.2F

def format_temperature(temperature):
    """
    This function formats the temperature to one decimal place followed by 'F'.

    :param temperature: float, the temperature to format
    :return: string, the formatted temperature with 'F' suffix
    """
    return f"{temperature:.1f}F"


def test_format_temperature():
    """
    This function tests the format_temperature function.
    """
    test_params = {
        101.193124: "101.2F",
        -100.123456: "-100.1F",
        0: "0.0F"
    }
    pass_count = 0
    fail_count = 0

    print("Testing format_temperature function:")
    print("-" * 70)
    for input_temp, expected in test_params.items():
        actual = format_temperature(input_temp)
        result = "Pass" if actual == expected else "Fail"
        print(
            f"Input: {input_temp}, Expected: {expected} | "
            f"Actual: {actual} | "
            f"Result: {result} |"
        )
        print("-" * 70)
        if actual == expected:
            pass_count += 1
        else:
            fail_count += 1
    print(f"Passed: {pass_count}, Failed: {fail_count}\n")


test_format_temperature()


# Task 2:
# Write a task that takes four 8-letter words from a user.
# You'll then need to use string slicing
# (including best practices to read characters
# from the end of a string backwards)
# to output in this manner:
# First three letters of the first word
# last four letters of the second word
# letters 4-6 of the third word
# letters 6-8 of the fourth word
# Example:
# Word 1: document
# Word 2: absolute
# Word 3: academic
# Word 4: birthday
# The output would be: doclutedemday

def word_scramble():
    """
    This function takes four 8-letter words from the user
    and creates a scrambled word
    by combining specific letters from each word.
    The first three letters of the first word,
    the last four letters of the second word,
    letters 4-6 of the third word,
    and letters 6-8 of the fourth word.
    """
    print("WORD SCRAMBLE FUN TIME!")
    print("Enter four 8-letter words to create a scrambled word.")
    print("-" * 70)
    word_list = []
    for i in range(1, 5):
        while True:
            word = input(f"Enter word {i}: ")
            if len(word) == 8:
                word_list.append(word)
                break
            else:
                print("Please enter an 8-letter word.")

    scrambled_word = (
        word_list[0][:3] +
        word_list[1][-4:] +
        word_list[2][3:6] +
        word_list[3][5:8]
    )
    print("-" * 70)
    print(f"Scrambled word: {scrambled_word}\n")


word_scramble()


# Task 3 (make sure you've worked through 7.4 of the zyBook):
# Use the string splitting method to take the same four words
# from Task 2 and output the result:
# Joining the words 1 and 3 together
# words 2 and 4 together - print the output
# Important: To make the string split/join approach work,
# you will need to programmatically merge the original words from Task 2
# while inserting some kind of delimiter.
# Then, programmatically split and join per the instructions in Task 3
# The output from the example above would be:
# documentacademic absolutebirthday
def word_split_join():
    """
    This function takes four 8-letter words from the user,
    merges them with a delimiter,
    and then splits and joins them as per the above instructions.
    """
    print("WORD SPLIT JOIN FUN TIME!")
    print("Enter four 8-letter words to create a merged string.")
    print("-" * 70)
    word_list = []
    for i in range(1, 5):
        while True:
            word = input(f"Enter word {i}: ")
            if len(word) == 8:
                word_list.append(word)
                break
            else:
                print("Please enter an 8-letter word.")

    merged_string = ",".join(word_list)
    print("-" * 70)
    split_words = merged_string.split(",")
    result = (
        split_words[0] + split_words[2] + " " + split_words[1] + split_words[3]
        )
    print(f"Result: {result}\n")


word_split_join()
