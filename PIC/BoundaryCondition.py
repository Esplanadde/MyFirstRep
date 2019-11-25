import numpy as np

class BC:
    def __init__(self, index=0):
        self.index = index

    def apply(self, E, B, t):
        E[self.index] = self.E_values(t)
        B[self.index] = self.B_values(t)

    def E_values(self, t):
        return 0, 0, 0

    def B_values(self, t):
        return 0, 0, 0