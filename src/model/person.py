from dataclasses import dataclass
from uuid import UUID


@dataclass
class Person:
    id: UUID
    name: str

