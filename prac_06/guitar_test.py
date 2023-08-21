from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 100)

    print(f"Gibson L-5 CES get_age() - Expected 101. Got {gibson.get_age()}")
    print(f"Another Guitar get_age() - Expected 10. Got {another_guitar.get_age()}")
    print()
    print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")


main()
