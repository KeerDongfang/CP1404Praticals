"""
CP1404/CP5632 Practical
Data file -> lists program
"""

from operator import itemgetter

FILENAME = "subject_data.txt"
nested_lists = []


def main():
    """Main function"""
    data = get_data()
    print(data)
    display_details()


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        nested_lists.append(parts)
        nested_lists.sort()
    input_file.close()
    return nested_lists


def display_details():
    """Print data in certain arrangement"""
    for i in range(len(nested_lists)):
        print(f"{nested_lists[i][0]} is taught by {nested_lists[i][1]} and has {nested_lists[i][2]} students.")


main()
