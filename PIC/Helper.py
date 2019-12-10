import numpy as np


def plasma_parameter(N_particles, N_grid, dx):
    return (N_particles / N_grid) * dx


def calculate_number_timesteps(T, dt):
    return int(T / dt) + 1


q = 4.8 * 10 ** (-10)
m = 1.67 * 10 ** (-27)
qm = q / m
cs = 3 * 10 ** 10
n = 1.0
T = 10.0**5
kb = 1.38 * 10 **(-16)
ld = np.sqrt((4 * np.pi * n * q**2) / (kb * T))
B0 = 10 ** (-4)



