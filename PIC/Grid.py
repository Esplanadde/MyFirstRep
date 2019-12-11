import numpy as np
import Helper as h
import random
import scipy.stats as st
import matplotlib.pyplot as plt

N_c = 10
N_p = 10

class Particle:
    def __init__(self):
        self.r = np.zeros(3)
        self.v = np.zeros(3)
        self.a = np.zeros(3)
        self.m_p = 1


class Cell():
    def __init__(self):
        self.N = 0
        self.particles = []
        self.X_c = 0
        self.size = 1
        self.weight = 0
        self.E = np.zeros(3)
        self.B = np.zeros(3)

    def add_particle(self, particle=Particle()):
        self.particles.append(particle)
        self.weight += self.particles[self.N].m_p
        self.N += 1

    def delete(self, delete_number):
        self.particles.pop(delete_number)
        self.weight -= self.particles[self.N].m_p
        self.N -= 1

    def Maxwell(self):
        maxwell = st.maxwell
        data = maxwell.rvs(scale=1, size=N_p)
        params = maxwell.fit(data, floc=0)
        datanew = maxwell.rvs(*params, size=1)
        return datanew


def get_cell_number(x, cells):
    for i in range(0, len(cells)):
        if (x >= cells[i].X_c - cells[i].size / 2) and (x < cells[i].X_c + cells[i].size / 2):
            return i


# create grid center coordinates array
def grid(N_c, x_min, x_max, cells=None):
    if cells is None:
        cells = []
    size = x_max - x_min
    dx = (size / N_c)
    for i in range(0, N_c):
        cells.append(Cell())
        cells[i].X_c = x_min + (dx * i) + (dx / 2)
        cells[i].size = dx
    return cells


CELLS = grid(N_c, 0.0, h.ld * N_c)

for i in range(0, N_p):
    x = random.uniform(0.0, h.ld * N_c)
    Part = Particle()
    Part.r[0] = x
    cell_number = get_cell_number(x, CELLS)
    CELLS[cell_number].add_particle(Part)


# Maxwell-velocity distributed
maxwell = np.zeros(N_p)
for j in range(0, N_p):
    maxwell[j] += CELLS[j].Maxwell()
