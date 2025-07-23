from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name, is_alive=True):
        """Initialize the King with a first name and alive status."""
        super().__init__(first_name, is_alive)
        # self.family_name = "King"
        # self.eyes = 'brown'
        # self.hairs = 'dark'

    def set_eyes(self, eyes):
        """Set the eye color of the King."""
        self.eyes = eyes

    def get_eyes(self):
        """Get the eye color of the King."""
        return self.eyes

    def set_hairs(self, hairs):
        """Set the hair color of the King."""
        self.hairs = hairs

    def get_hairs(self):
        """Get the hair color of the King."""
        return self.hairs


Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
