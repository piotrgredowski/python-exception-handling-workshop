from dataclasses import dataclass

from .person import Person


@dataclass
class Todo:
    text: str
    assignee: Person
