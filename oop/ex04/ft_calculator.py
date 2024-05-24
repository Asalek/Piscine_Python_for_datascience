class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''dotProduct return total of V1+V2 of each column'''
        tot = 0
        for i in range(len(V1)):
            tot += (V1[i] * V2[i])
        print(f"Dot product is : {tot}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''add_vec Adds V1 to V2 and print it'''
        vec = []
        for i in range(len(V1)):
            vec.append(float(V1[i] + V2[i]))
        print(f"Add Vector is : {vec}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''sous_vec substrac V2 from V1'''
        vec: float = []
        for i in range(len(V1)):
            vec.append(float(V1[i] - V2[i]))
        print(f"Sous Vector is: {vec}")
