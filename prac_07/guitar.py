CURRENT_YEAR = 2023
VINTAGE_YEAR = 50


class Guitar:
    """create class"""

    def __init__(self, name, year, cost):
        """initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """string format function"""
        return f"{self.name}({self.year}): ${self.cost}"

    def get_age(self):
        """get the age of a guitar"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """to check if the guitar is vintage or not"""
        return self.get_age() >= VINTAGE_YEAR
