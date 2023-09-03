from guitar import Guitar


def main():
    guitars = []
    with open('guitars.csv', 'r') as file:
        lines = file.readlines()
        for line in lines:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort(key=lambda x: x.year)
    print("These are my guitars sorted by year:")
    display_guitars(guitars)

    add_new_guitar(guitars)

    write_guitars_to_file(guitars)


def add_new_guitar(guitars):
    name = input("Enter guitar name (or 'q' to quit): ")
    while name.lower() != 'q':
        year = int(input("Enter manufacturing year: "))
        cost = float(input("Enter cost: "))
        guitars.append(Guitar(name, year, cost))
        name = input("Enter guitar name (or 'q' to quit): ")


def display_guitars(guitars):
    """Display all the guitars"""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f}")


def write_guitars_to_file(filename, guitars):
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()
