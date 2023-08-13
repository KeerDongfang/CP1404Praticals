FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """main function"""
    datas = get_data(FILENAME)
    champion_to_count, countries = process_records(datas)
    display_results(champion_to_count, countries)


def get_data(filename):
    """Get datas from file."""
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            champions_data.append(parts)
    return champions_data


def process_records(datas):
    """extract needed information"""
    champion_counts = {}
    countries = set()
    for data in datas:
        countries.add(data[COUNTRY_INDEX])
        try:
            champion_counts[data[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_counts[data[CHAMPION_INDEX]] = 1
    return champion_counts, countries


def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(country for country in sorted(countries)))


main()
