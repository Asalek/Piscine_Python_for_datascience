import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


def Create_login(name: str, surName: str) -> str:
    if (name == "" or surName == ""):
        return "".join(random.choices(string.ascii_lowercase, k=4))
    return f"{name[0]}{surName}"


@dataclass  # __init, repr, eq__
class Student:
    name: str = ""
    surname: str = ""
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = Create_login(self.name, self.surname)


# @property CAN read but not write
# def get_a(self):
#     return self.a

# order=True : __lt, le, gt, ge__()

# default_factory: create Immutable object, can't change
# default        : create mutable object, can be changed after creation

# __post_init__ : called after init is done to use the init Vars.
