from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """Your docstring for die"""
        self.is_alive = False

    def __str__(self):
        """Your docstring for __str__"""
        return f"Vector: is {'alive' if self.is_alive else 'dead'}"

    def __repr__(self):
        """Your docstring for __repr__"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """Your docstring for __str__"""
        return f"Vector: is {'alive' if self.is_alive else 'dead'}"

    def __repr__(self):
        """Your docstring for __repr__"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __doc__(self):
        """Your docstring for __doc__"""
        return "This is a Lannister character."

    def die(self):
        """Your docstring for die"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Your docstring for create_lannister"""
        return cls(first_name, is_alive)


# Robert = Baratheon("Robert")
# print(Robert.__dict__)
# print(Robert.__str__)
# print(Robert.__repr__)
# print(Robert.is_alive)
# Robert.die()
# print(Robert.is_alive)
# print(Robert.__doc__)
# print("---")
# Cersei = Lannister("Cersei")
# print(Cersei.__dict__)
# print(Cersei.__str__)
# print(Cersei.is_alive)
# print("---")
# Jaine = Lannister.create_lannister("Jaine", True)
# typ = (Jaine.first_name, type(Jaine).__name__)
# string = f"Name : {typ}, Alive : {Jaine.is_alive}"
# print(string)
