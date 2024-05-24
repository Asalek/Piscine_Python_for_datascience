from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    '''King Class'''

    def set_eyes(self, color: str):
        '''Set eye color Doc'''
        self.eyes = color

    def set_hairs(self, color: str):
        '''Set hair color Doc'''
        self.hairs = color

    def get_eyes(self) -> str:
        '''Get hair color Doc'''
        return self.eyes

    def get_hairs(self) -> str:
        '''Get hair color Doc'''
        return self.hairs
