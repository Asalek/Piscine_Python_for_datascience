from abc import ABC, abstractmethod


class Character(ABC):
    """Character Abstract Class"""
    def __init__(self, first_name: str, is_alive=True) -> None:
        """Object with FName and is_alive status """
        if not isinstance(first_name, str):
            raise TypeError("First Name MUST BE a String")
        if not isinstance(is_alive, bool):
            raise TypeError("is_alive MUST be boolean")
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die():
        '''Character die'''
        Ellipsis  # ...


class Stark(Character):
    """Stark Class inheret from Character One"""

    def die(self):
        '''Start Die function switchs is_alive to False'''
        self.is_alive = False
