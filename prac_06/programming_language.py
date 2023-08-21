class ProgrammingLanguage:
    """create class"""

    def __init__(self, name, typing, reflection, year):
        """initialise class"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """to check if the typing of a language is dynamic or not"""
        if self.typing == "Dynamic":
            return self.name

    def __str__(self):
        """string format function"""
        return f"{self.name}, {self.typing} typing, Reflection = {self.reflection}, First appeared in {self.year}"
