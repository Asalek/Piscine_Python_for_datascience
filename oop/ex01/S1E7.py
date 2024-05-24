from S1E9 import Character


class Baratheon(Character):
    '''Representing The Baratheon Family'''

    def __init__(self, first_name: str, is_alive=True,
                 family_name: str = 'Baratheon', eyes: str = 'brown',
                 hairs: str = 'dark') -> None:
        '''Baratheon __init__ '''
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        '''Baratheon __str__ '''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        '''Baratheon __repr__'''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def die(self):
        '''Start Die function switchs is_alive to False'''
        self.is_alive = False


class Lannister(Character):
    '''Representing The Lannister Family'''
    def __init__(self, first_name: str, is_alive=True,
                 family_name: str = 'Lannister', eyes: str = 'blue',
                 hairs: str = 'light') -> None:
        '''Lannister __init__ '''
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        '''Lannister __str__ '''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def __repr__(self) -> str:
        '''Lannister __repr__'''
        return f'Vector: ({self.family_name}, {self.eyes}, {self.hairs})'

    def die(self):
        '''Start Die function switchs is_alive to False'''
        self.is_alive = False
    # @classmethod
    # can access and manipulate attribu,first param is always the class itself

    @staticmethod  # knows nothing about the class methods or attributes
    def create_lannister(first_name: str, is_alive=True):
        '''Create Lannister's Children'''
        return Lannister(first_name, is_alive)

#  Docs:
#   __str__ AND __repe__ : https://www.youtube.com/watch?v=FIaPZXaePhw
