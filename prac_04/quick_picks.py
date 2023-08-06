import random

numbers_per_line = 6
minimum_number = 1
maximum_number = 45


def main():
    """main function"""
    number_of_line = int(input("How many quick picks?: "))
    number_of_line = error_checking(number_of_line)
    quick_pick_program(number_of_line)


def error_checking(number_of_line):
    """check if the input is valid"""
    while number_of_line < 0:
        print("Invalid input.")
        number_of_line = int(input("How many quick picks?: "))
    return number_of_line


def quick_pick_program(number_of_line):
    """quick qick program"""
    for i in range(number_of_line):
        quick_pick = []
        for n in range(numbers_per_line):
            number = random.randint(minimum_number, maximum_number)
            while number in quick_pick:
                number = random.randint(minimum_number, maximum_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()





