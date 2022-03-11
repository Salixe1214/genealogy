from typing import List
from datetime import date

class Person():
    def __init__(self, firstName: str, lastName: str, birth: date) -> None:
        self.firstName: str             = firstName
        self.lastName: str              = lastName
        self.fullName: str              = f'{self.firstName} {self.lastName}'
        self.birthDate: date            = birth
        self.parents: List[Person]      = []
        self.children: List[Person]     = []
        self.conjoint: Person or None   = None

    def __str__(self) -> str:
        return self.fullName

    def __add__(self, other):
        assert type(self) == type(other)
        self.children.append(other)
        other.parents.append(self)
        return self

    def __repr__(self) -> str:
        return self.fullName

    def __eq__(self, other) -> bool:
        return self.fullName == other.fullName and self.birthDate == other.birthDate

    def __gt__(self, other):
        return self.birthDate > other.birthDate

    def __contains__(self, item) -> bool:
        if item in self.parents or item in self.children:
            return True

        for relative in self.parents + self.children:
            return item in relative



