import random
import string
from dataclasses import dataclass


def generate_id() -> str:
    """Generate a random 15-character string ID."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class representing a student."""
    def __init__(self, name, surname, is_active=True):
        self.id = generate_id()
        self.name = name
        self.surname = surname
        self.is_active = is_active
        self.id = generate_id()
        self.login = self.name[0] + self.surname

    def __str__(self):
        """Return a string representation of the student."""
        return f"Student(name={self.name}, surname={self.surname}, \
is_active={self.is_active}, login={self.login}, id={self.id})"

    def __repr__(self):
        """Return a detailed string representation of the student."""
        return f"Student(name={self.name}, surname={self.surname},\
 is_active={self.is_active}, login={self.login}, id={self.id})"
