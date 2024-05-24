class calculator:
    '''Calculator doc'''

    def __init__(self, vec: list[float | int]):
        '''Calculator docs'''
        self.vec = vec

    def __add__(self, object) -> None:
        '''add doc'''
        for i in range(len(self.vec)):
            self.vec[i] += object
        print(self.vec)

    def __mul__(self, object) -> None:
        '''mul doc'''
        for i in range(len(self.vec)):
            self.vec[i] *= object
        print(self.vec)

    def __sub__(self, object) -> None:
        '''sub doc'''
        for i in range(len(self.vec)):
            self.vec[i] -= object
        print(self.vec)

    def __truediv__(self, object) -> None:
        '''div doc'''
        if object == 0:
            raise ZeroDivisionError
        for i in range(len(self.vec)):
            self.vec[i] /= object
        print(self.vec)
