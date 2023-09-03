import random

PLACES_CSV_FILE = "places.csv"


def display_menu():
    """Menu for the program"""
    print("Menu:")
    print("L. List places")
    print("R. Recommend a place to visit")
    print("A. Add a new place")
    print("M. Mark a place as visited")
    print("Q. Quit")


def load_places_data():
    """read the file that contain needed information"""
    places = []
    try:
        with open(PLACES_CSV_FILE, "r") as file:
            for line in file:
                name, country, priority, visited = line.strip().split(",")
                places.append([name, country, int(priority), visited])
        return places
    except FileNotFoundError:
        return []


def list_places(places):
    """Sort the list based on the length of names"""
    sorted_places = sorted(places, key=lambda place: len(place[0]))

    max_country_length = max(len(place[1]) for place in sorted_places)

    unvisited_count = sum(1 for place in sorted_places if place[3] == "n")
    print(f"Total places: {len(sorted_places)}, Unvisited places: {unvisited_count}")

    for place in sorted_places:
        visited_marker = "*" if place[3] == "n" else " "
        print(
            f"{visited_marker} {place[0]:<{len(sorted_places[-1][0])}} | {place[1]:<{max_country_length}} | Priority: {place[2]}")

    print(f"{len(sorted_places)} places. You still want to visit {unvisited_count} places.")


def recommend_place(places):
    """randomly recommend a place for visiting"""
    unvisited_places = [place for place in places if place[3] == "n"]
    if not unvisited_places:
        print("No places left to visit!")
    else:
        random_place = random.choice(unvisited_places)
        print(f"You might consider visiting: {random_place[0]} in {random_place[1]}")


def add_place(places):
    """add place and other information to the list"""
    valid_input = False

    while not valid_input:
        name = input("Enter the place's name: ")
        country = input("Enter the country: ")

        try:
            priority = int(input("Enter the priority: "))
        except ValueError:
            print("Priority must be a valid integer. Please enter a valid priority.")
            continue

        if name.strip() and country.strip():
            new_place = [name, country, priority, "n"]
            places.append(new_place)
            print("Place added successfully!")
            valid_input = True
        else:
            print("Name and country cannot be blank. Please enter valid values.")


def mark_visited(places):
    """mark unvisited place as visited"""
    unvisited_places = [place for place in places if place[3] == "n"]
    if not unvisited_places:
        print("No unvisited places.")
    else:
        print("Unvisited places:")
        for idx, place in enumerate(unvisited_places, start=1):
            print(f"{idx}. {place[0]} in {place[1]}")

        choice = int(input("Enter the number of the place to mark as visited: ")) - 1
        while 0 > choice or choice > len(unvisited_places) - 1:
            print("Invalid input, please try again.")
            choice = int(input("Enter the number of the place to mark as visited: ")) - 1
        unvisited_places[choice][3] = "v"
        print(f"{unvisited_places[choice][0]} marked as visited!")


def save_places_data(places):
    """save the file"""
    with open(PLACES_CSV_FILE, "w") as file:
        for place in places:
            file.write(f"{','.join(map(str, place))}\n")
    print("Places saved to CSV!")


def main():
    """main function"""
    print("Welcome to the Travel Tracker!")
    places = load_places_data()

    display_menu()
    choice = input("Enter your choice: ").upper()

    while choice != "Q" and choice != " " and choice != "5":
        if choice == "L" or choice == "1":
            list_places(places)
        elif choice == "R" or choice == "2":
            recommend_place(places)
        elif choice == "A" or choice == "3":
            add_place(places)
        elif choice == "M" or choice == "4":
            mark_visited(places)
        else:
            print("Invalid choice. Please choose a valid option.")
        display_menu()
        choice = input("Enter your choice: ").upper()
    save_places_data(places)
    print("Thank you for using Travel Tracker!")


main()
