minimum_score = 0
maximum_score = 100
stander_of_excellent = 90
stander_of_pass = 50

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""


def main():
    print(MENU)
    menu_choice = input("Please enter your choice: ").upper()

    while menu_choice != 'Q':
        if menu_choice == 'G':
            score = float(input("Please enter your score:"))
            get_valid_score(score)
        elif menu_choice == 'P':
            determine_grade(score)
        elif menu_choice == 'S':
            show_stars(score)
        menu_choice = input("Please enter your choice: ").upper()
    print("Goodbye.")


def get_valid_score(score):
    """determine if the score is valid"""
    if score < minimum_score or score > maximum_score:
        print("Invalid score.")


def determine_grade(score):
    """determine the grade by score"""
    if score < minimum_score or score > maximum_score:
        print("Invalid score.")
    elif score >= stander_of_excellent:
        print("Excellent.")
    elif score >= stander_of_pass:
        print("Pass.")
    else:
        print("Bad")


def show_stars(score):
    """print as many stars as the score"""
    stars = '*' * int(score)
    print(stars)


main()
