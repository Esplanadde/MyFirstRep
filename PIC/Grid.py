import numpy as np
import Helper as h
import random
import scipy.stats as st
import matplotlib.pyplot as plt


def Maxwell(v, T):
    return np.sqrt(h.m/(2*np.pi*h.kb*T))*np.exp(-(h.m*v*v)/(2*h.kb*T))


def invert_Maxwell(F, T):
    speed = (1/(-h.m))*2*h.kb*T*np.log(F/np.sqrt(h.m/(2*np.pi*h.kb*T)))
    return speed


def get_rand_maxwell(T):
    F = random.uniform(0.0, 1.0)
    v = invert_Maxwell(F, T)
    return v



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


N_c = 10
N_p = 10

CELLS = grid(N_c, 0.0, h.ld * N_c)

for i in range(0, N_p):
    x = random.uniform(0.0, h.ld * N_c)
    Part = Particle()
    Part.r[0] = x
    cell_number = get_cell_number(x, CELLS)
    CELLS[cell_number].add_particle(Part)

speeds = np.zeros(100)
for i in range(0,100):
    speeds[i] = get_rand_maxwell(h.T)


print(speeds)
