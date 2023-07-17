import random

minimum_score = 0
maximum_score = 100
stander_of_excellent = 90
stander_of_pass = 50


def main():
    score = float(input("Enter score: "))
    determine_grade(score)
    score = random.randint(minimum_score, maximum_score)
    print(f"The random score is {score}.")
    determine_grade(score)


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


main()
